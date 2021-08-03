class Solution:
    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        m = len(nums1)
        n = len(nums2)
        mod = 10**9 + 7
        pre1 = [0] * (m + 1)
        pre2 = [0] * (n + 1)

        for i in range(m):
            pre1[i + 1] = pre1[i] + nums1[i]
        for i in range(n):
            pre2[i + 1] = pre2[i] + nums2[i]

        cm1 = []
        cm2 = []
        st = set()
        d = {}
        for i in range(m):
            d[nums1[i]] = i
        st1 = set(nums1)
        # print(st)
        for i in range(n):
            if nums2[i] in st1:
                cm1.append(d[nums2[i]])
                cm2.append(i)
        ans = 0
        # print(pre1,pre2,cm1,cm2)
        for i in range(len(cm1)):
            idx1 = cm1[i]
            idx2 = cm2[i]

            if i == 0:
                sm1 = pre1[idx1]
                sm2 = pre2[idx2]
            else:
                sm1 = pre1[idx1] - pre1[cm1[i - 1] + 1]
                sm2 = pre2[idx2] - pre2[cm2[i - 1] + 1]
            ans += max(sm1, sm2)
            ans %= mod
        op1 = 0
        op2 = 0
        if len(cm1) and cm1[-1] + 1 < m:
            op1 = sum(nums1[cm1[-1] + 1:])
        if len(cm2) and cm2[-1] + 1 < n:
            op2 = sum(nums2[cm2[-1] + 1:])
        if not len(cm1):
            return (max(sum(nums1), sum(nums2))) % mod
        ans += max(op1, op2)
        ans %= mod
        return (ans + sum(nums1[i] for i in cm1)) % mod
