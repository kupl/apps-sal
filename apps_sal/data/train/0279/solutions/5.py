class Solution:
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        nums = [i + 1 for i in range(0, n)]

        def nextnum(nn):
            cnt = 0
            for i in range(0, len(nums)):
                if nums[i] == 0:
                    continue
                cnt += 1
                if cnt == nn:
                    ret = nums[i]
                    nums[i] = 0
                    return ret

        facts = [1]
        for i in range(1, n + 2):
            facts.append(facts[i - 1] * i)
        perm = []
        while (n > 1):
            nk = (k - 1) // facts[n - 1] + 1
            rk = (k - 1) % facts[n - 1] + 1
            perm.append(nextnum(nk))
            k = rk
            n -= 1
        perm.append(nextnum(k))
        return "".join([str(x) for x in perm])
