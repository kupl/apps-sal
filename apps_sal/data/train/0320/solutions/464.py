class Solution:

    def soln(self, nums, ans, e, o):
        if len(nums) == 0:
            return ans
        for i in nums:
            if i % 2 == 0 and i != 0:
                e.append(i)
            elif i != 0:
                o.append(i)
        ans += len(o)
        for i in range(len(o)):
            o[i] -= 1
        oo = []
        for i in range(len(o)):
            if o[i] != 0:
                oo.append(o[i])
        o = oo.copy()
        for i in range(len(o)):
            o[i] = int(o[i] / 2)
        if len(e) != 0 or len(o) != 0:
            ans += 1
        for i in range(len(e)):
            e[i] = int(e[i] / 2)
        nnu = []
        for i in e:
            if i != 0:
                nnu.append(i)
        for i in o:
            if i != 0:
                nnu.append(i)
        return self.soln(nnu, ans, [], [])

    def minOperations(self, nums: List[int]) -> int:
        e = []
        o = []
        ans = 0
        return self.soln(nums, ans, e, o)
