class Solution:
    def minJumps(self, arr: List[int]) -> int:
        map = collections.defaultdict(list)
        for i, a in enumerate(arr):
            map[a].append(i)
        
        visited, visiting = {-1}, {0}
        for steps in itertools.count():
            visited |= visiting
            if len(arr) - 1 in visited:
                return steps
            visiting = {j for i in visiting for j in [i - 1, i + 1] + map.pop(arr[i], [])} - visited
