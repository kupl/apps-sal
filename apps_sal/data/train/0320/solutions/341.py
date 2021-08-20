class Solution:

    def minOperations(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        q = collections.deque()
        q += [(0, nums)]
        tot = [0] * n
        while q:
            (cnt, t) = q.popleft()
            if t == tot:
                return cnt
            flag = False
            for i in range(n):
                if t[i] % 2:
                    cnt += 1
                    t[i] -= 1
                if t[i] != 0:
                    flag = True
                t[i] //= 2
            if flag:
                cnt += 1
            q += [(cnt, t)]
        return 0
