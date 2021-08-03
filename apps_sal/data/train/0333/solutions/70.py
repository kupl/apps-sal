class Solution:
    def minJumps(self, arr: List[int]) -> int:

        if len(arr) == 1:
            return 0

        # prune duplicates
        i = 0
        while i < len(arr) - 2:
            if arr[i] == arr[i + 1] == arr[i + 2]:
                arr.pop(i)
            else:
                i += 1

        def jump(i):
            nexts = []
            if i - 1 >= 0:
                nexts.append(i - 1)
            if i + 1 < len(arr):
                nexts.append(i + 1)
            for index in d[arr[i]]:
                #print('index', index)
                if index != i:
                    nexts.append(index)
            return nexts

        d = {}
        for i in range(len(arr) - 1, -1, -1):
            if arr[i] in d:
                d[arr[i]].add(i)
            else:
                d[arr[i]] = {i}  # value is set

        for k, v in list(d.items()):
            d[k] = list(v)
            d[k].sort(reverse=True)
        q = deque()

        visited = set()
        q.append(0)
        visited.add(0)
        steps = -1
        while q:
            size = len(q)
            steps += 1
            for i in range(size):
                pop_index = q.popleft()
                if pop_index == len(arr) - 1:
                    return steps
                for nex in jump(pop_index):
                    if nex not in visited:
                        q.append(nex)
                        visited.add(nex)
        return -1
