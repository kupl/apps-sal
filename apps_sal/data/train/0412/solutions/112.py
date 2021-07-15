class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        def helper(d, target, map):
            if (d,target) in map:
                return map[(d,target)]
            if d == target:
                return 1
            elif d == 0 or target < d:
                return 0
            map[(d,target)] = 0
            for num in range(1,f+1):
                map[(d,target)] += helper((d-1), (target-num), map)
            return map[(d,target)]
        helperMap = {}
        return (helper(d,target,helperMap)%(10**9+7))
