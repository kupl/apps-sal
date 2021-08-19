class Solution:

    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        dic = collections.defaultdict(list)
        for (i, num) in enumerate(arr):
            dic[num].append(i)
        queue = [0]
        pos_visited = set([0])
        num_visited = set()
        step = 0
        while queue:
            for _ in range(len(queue)):
                cur = queue.pop(0)
                if cur == n - 1:
                    return step
                for nextIdx in [cur - 1, cur + 1] + dic[arr[cur]] * (arr[cur] not in num_visited):
                    if 0 <= nextIdx < n and nextIdx not in pos_visited:
                        pos_visited.add(nextIdx)
                        queue.append(nextIdx)
                num_visited.add(arr[cur])
            step += 1
        return -1
