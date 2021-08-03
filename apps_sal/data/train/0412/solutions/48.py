class Solution:
    def helper(self, d, f, target):
        if(d == 0):
            if(target == 0):
                return 1
            else:
                return 0

        if((d, target) in self.memo):
            return self.memo[(d, target)]

        count = 0
        for i in reversed(list(range(1, min(target + 1, f + 1)))):
            count += self.helper(d - 1, f, target - i)

        self.memo[(d, target)] = count
        return count

    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        self.memo = dict()
        return self.helper(d, f, target) % (10**9 + 7)
