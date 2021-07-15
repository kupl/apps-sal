class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        rsum = []
        for i in range(n):
            sums = [nums[i]]
            for j in range(i+1, n):
                sums.append(sums[-1] + nums[j])
            rsum.append(sums)
        def merge(arr1, arr2):
            i1 = i2 = 0
            arr = []
            while True:
                if arr1[i1] <= arr2[i2]:
                    arr.append(arr1[i1])
                    i1 += 1
                    if i1 >= len(arr1):
                        for j in range(i2, len(arr2)):
                            arr.append(arr2[j])
                        return arr
                else:
                    arr.append(arr2[i2])
                    i2 += 1
                    if i2 >= len(arr2):
                        for j in range(i1, len(arr1)):
                            arr.append(arr1[j])
                        return arr
        #print(rsum)
        while len(rsum) >= 2:
            rsum_new = []
            i = 0
            while i < len(rsum) - 1:
                rsum_new.append(merge(rsum[i], rsum[i+1]))
                i += 2
            if i < len(rsum):
                rsum_new.append(rsum[i])
            rsum = rsum_new
        v = 0
        rsum = rsum[0]
        #print(rsum)
        for i in range(left-1, right):
            v += rsum[i]
        return v % (10**9+7)

