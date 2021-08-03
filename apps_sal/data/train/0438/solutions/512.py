from collections import defaultdict


class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        parent = {}
        rank = defaultdict(int)
        size = {}

        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            nx, ny = find(x), find(y)

            if nx == ny:
                return False

            if rank[nx] > rank[ny]:
                parent[ny] = nx
                size[nx] += size[ny]
                return size[nx]
            elif rank[nx] > rank[ny]:
                parent[nx] = ny
                size[ny] += size[nx]
                return size[ny]
            else:
                parent[nx] = ny
                rank[ny] += 1
                size[ny] += size[nx]
                return size[ny]

        seen = set()
        last = -1
        size_counts = Counter()

        for i, num in enumerate(arr):
            parent[num] = num
            size[num] = 1
            if num - 1 in seen and num + 1 in seen:
                size_counts[size[find(num - 1)]] -= 1
                size_counts[size[find(num + 1)]] -= 1
                union(num - 1, num)
                res = union(num + 1, num)
                size_counts[res] += 1
            elif num - 1 in seen:
                size_counts[size[find(num - 1)]] -= 1
                res = union(num - 1, num)
                size_counts[res] += 1
            elif num + 1 in seen:
                size_counts[size[find(num + 1)]] -= 1
                res = union(num + 1, num)
                size_counts[res] += 1
            else:
                size_counts[size[num]] += 1

            if m in size_counts and size_counts[m] > 0:
                last = i + 1
            # for _, l in parent.items():
            #     if size[find(l)] == m:
            #         last = i + 1

            seen.add(num)
        return last
