class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:

        N = len(nums)
        l = []

        for i in range(N):
            s = 0
            for j in range(i, N):
                s += nums[j]
                l.append(s)
        totsum = sum(l)
        self.quickselect(l, 0, len(l) - 1, left)
        s1 = sum(l[:left - 1])
        self.quickselect(l, 0, len(l) - 1, right)
        s2 = sum(l[right:])
        return (totsum - s1 - s2) % (10**9 + 7)

    def quickselect(self, arr, l, h, k):
        if(l >= h):
            return
        mid = int((l + h) / 2)
        x = arr[mid]
        l1, h1 = self.partition(arr, l, h, x)
        if(k >= l1 + 1 and k <= h1 + 1):
            return
        elif(k < l1 + 1):
            return self.quickselect(arr, l, l1 - 1, k)
        else:
            return self.quickselect(arr, h1 + 1, h, k)

    def partition(self, arr, l, h, x):
        l1 = l
        h1 = h
        m1 = l
        while(m1 <= h1):
            if(arr[m1] == x):
                m1 += 1
            elif(arr[m1] < x):
                arr[l1], arr[m1] = arr[m1], arr[l1]
                l1 += 1
                m1 += 1
            else:
                arr[h1], arr[m1] = arr[m1], arr[h1]
                h1 -= 1
        return l1, h1
