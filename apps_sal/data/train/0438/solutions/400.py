class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        N = len(arr)
        arr = [x - 1 for x in arr]
        parent = [x for x in range(N)]
        size = [1 for _ in range(N)]
        used = [False for _ in range(N)]

        def ufind(a):
            if a == parent[a]:
                return a
            parent[a] = ufind(parent[a])
            return parent[a]

        def uunion(a, b):
            sa = ufind(a)
            sb = ufind(b)

            if sa != sb:
                parent[sa] = parent[sb]
                size[sb] += size[sa]

        def usize(a):
            return size[ufind(a)]

        counts = [0] * (N + 1)

        latest = -1
        for index, x in enumerate(arr):
            left = 0
            if x - 1 >= 0 and used[x - 1]:
                left = usize(x - 1)

            right = 0
            if x + 1 < N and used[x + 1]:
                right = usize(x + 1)

            current = 1
            counts[1] += 1
            if left > 0:
                counts[left] -= 1
            if right > 0:
                counts[right] -= 1
            counts[1] -= 1
            used[x] = True

            new_size = left + right + current
            counts[new_size] += 1
            if left > 0:
                uunion(x, x - 1)
            if right > 0:
                uunion(x, x + 1)

            if counts[m] > 0:
                latest = max(latest, index + 1)
        return latest
