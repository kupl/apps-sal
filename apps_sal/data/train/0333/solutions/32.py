# 1345. Jump Game IV
class Solution:
    def minJumps(self, arr: List[int]) -> int:
        maps = collections.defaultdict(list)
        [maps[a].append(i) for i, a in enumerate(arr)]
 
        begins = set([0])
        ends = set([len(arr) - 1])
        visitedIdx = set([-1, len(arr)])
        for steps in range(len(arr)):
            if len(begins) > len(ends):
                begins, ends = ends, begins
            nextLevels = set()
            for b in begins:
                if b in ends:
                    return steps
                if b in visitedIdx:
                    continue
                visitedIdx.add(b)
                nextLevels.update([b - 1, b + 1] + maps[arr[b]])
                maps.pop(arr[b])
            begins = nextLevels
