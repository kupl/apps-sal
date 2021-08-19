class Solution:

    def findLatestStep(self, arr: List[int], m: int) -> int:
        arr = [a - 1 for a in arr]
        N = len(arr)
        state = [False for _ in range(N)]
        heads = [i for i in range(N)]
        children = {i: [i] for i in range(N)}
        counts = {0: N}
        last = -1
        for (it, x) in enumerate(arr):
            state[x] = True
            neighbors = [i for i in [x + 1, x - 1] if 0 <= i < N and state[i]]
            counts[0] -= 1
            if not neighbors:
                counts[1] = counts.get(1, 0) + 1
                if counts.get(m, 0) > 0:
                    last = it
                continue
            neighbors.sort(key=lambda x: len(children[heads[x]]))
            h = heads[neighbors[0]]
            heads[x] = h
            counts[len(children[h])] -= 1
            children[h].append(x)
            if len(neighbors) == 2:
                h2 = heads[neighbors[1]]
                for y in children[h2]:
                    heads[y] = h
                    children[h].append(y)
                counts[len(children[h2])] -= 1
            counts[len(children[h])] = counts.get(len(children[h]), 0) + 1
            if counts.get(m, 0) > 0:
                last = it
        if last == -1:
            return -1
        return last + 1
