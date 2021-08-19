class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        nums1.sort()
        nums2.sort()

        def ok(n, sorted_lst):
            i, j = 0, len(sorted_lst) - 1
            ret = 0
            #print(n, sorted_lst)
            while 0 <= i < j < len(sorted_lst):
                t = sorted_lst[i] * sorted_lst[j]
                if t > n:
                    j -= 1
                    while i < j < len(sorted_lst) - 1 and sorted_lst[j] == sorted_lst[j + 1]:
                        j -= 1
                elif t < n:
                    i += 1
                    while 0 < i < j and sorted_lst[i] == sorted_lst[i - 1]:
                        i += 1
                elif sorted_lst[i] == sorted_lst[j]:  # reach center elements
                    #print(n, sorted_lst[i])
                    ret += (j - i + 1) * (j - i) // 2
                    break
                else:
                    #print(n, i,j,sorted_lst[i],sorted_lst[j])
                    a, b = 1, 1
                    i += 1
                    while 0 < i < j and sorted_lst[i] == sorted_lst[i - 1]:
                        i += 1
                        a += 1
                    j -= 1
                    # print(i,j,sorted_lst[j])
                    while i <= j < len(sorted_lst) - 1 and sorted_lst[j] == sorted_lst[j + 1]:
                        j -= 1
                        b += 1
                    #print(a,b, a*b)
                    ret += a * b

            return ret

        tot, cur = 0, 0
        for i, v in enumerate(nums1):
            if i == 0 or v != nums1[i - 1]:
                cur = ok(v * v, nums2)
            tot += cur

        for i, v in enumerate(nums2):
            if i == 0 or v != nums2[i - 1]:
                cur = ok(v * v, nums1)
            tot += cur
        return tot
