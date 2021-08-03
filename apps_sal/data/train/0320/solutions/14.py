class Solution:
    def minOperations(self, nums: List[int]) -> int:
        x = [0] * len(nums)
        counts = 0
        while(1):
            counts += sum(n % 2 for n in nums)
            nums = [n // 2 for n in nums]
            if (nums == x):
                return counts
            counts += 1

        def div(l):
            for i in range(len(l)):
                if (sum(l) == 0):
                    return None
                l[i] *= 2
            return l

        def mi(l):
            for i in range(len(l)):
                l[i] += 1
            return l

        q = deque()

        q.append([0] * len(nums))
        d = 0
        while q:
            d += 1
            for i in range(len(q)):
                x = q.popleft()
                j = x.copy()
                print(x)
                if (x == nums):
                    return d
                y = div(j)
                if (y != None):
                    q.append(y)
                q.append(mi(x))
