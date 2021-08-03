class Solution:
    def minJumps(self, arr: List[int]) -> int:
        map = defaultdict(list)
        for i, item in enumerate(arr):
            map[item].append(i)

        q = deque()
        q.appendleft((0, 0))
        visited = set()
        num_vis = set()
        while q:
            index, jumps = q.pop()
            if index == len(arr) - 1:
                return jumps
            visited.add(index)
            if arr[index] not in num_vis:
                nxts = map[arr[index]]
                num_vis.add(arr[index])

                for nxt in nxts:
                    if nxt < 0 or nxt > len(arr) or nxt in visited:
                        continue
                    q.appendleft((nxt, jumps + 1))

            for nbr in [index + 1, index - 1]:
                if nbr < 0 or nbr >= len(arr) or nbr in visited:
                    continue
                q.appendleft((nbr, jumps + 1))

        return -1
