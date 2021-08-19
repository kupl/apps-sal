class Solution:

    def findLatestStep(self, arr: List[int], m: int) -> int:
        parents = {}
        weights = {}

        def find(p):
            if p not in parents:
                parents[p] = p
                weights[p] = 1
            if parents[p] != p:
                parents[p] = find(parents[p])
            return parents[p]

        def union(p, q):
            (i, j) = (find(p), find(q))
            if i == j:
                return
            if weights[i] >= weights[j]:
                parents[j] = i
                weights[i] += weights[j]
            else:
                parents[i] = j
                weights[j] += weights[i]

        def connected(p, q):
            return find(p) == find(q)
        status = [0] * len(arr)
        cnt = collections.Counter()
        last = -1
        for (step, info) in enumerate(arr):
            i = info - 1
            status[i] = 1
            if i == 0 or status[i - 1] == 0:
                left = False
            else:
                left = True
            if i >= len(arr) - 1 or status[i + 1] == 0:
                right = False
            else:
                right = True
            if not left and (not right):
                cnt[1] += 1
                p = find(arr[i])
            elif left and right:
                pleft = find(arr[i - 1])
                pright = find(arr[i + 1])
                size_left = weights[pleft]
                size_right = weights[pright]
                cnt[size_left] -= 1
                cnt[size_right] -= 1
                cnt[size_left + size_right + 1] += 1
                union(arr[i - 1], arr[i])
                union(arr[i], arr[i + 1])
            elif left:
                pleft = find(arr[i - 1])
                size_left = weights[pleft]
                cnt[size_left] -= 1
                cnt[size_left + 1] += 1
                union(arr[i - 1], arr[i])
            elif right:
                pright = find(arr[i + 1])
                size_right = weights[pright]
                cnt[size_right] -= 1
                cnt[size_right + 1] += 1
                union(arr[i], arr[i + 1])
            if cnt[m] > 0:
                last = step + 1
        return last
