class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        n = len(arr)
        if m == n:
            return n
        size = [0] * (n + 1)
        parents = list(range(n + 1))

        def find(x):
            if parents[x] != x:
                parents[x] = find(parents[x])
            return parents[x]

        def union(x, y):
            px, py = find(x), find(y)
            if size[px] < size[py]:
                px, py = py, px
            parents[py] = px
            size[px] += size[py]

        result = -1
        for j, i in enumerate(arr):
            size[i] = 1
            if i > 1 and size[find(i - 1)] == m:
                result = j
            if i < n and size[find(i + 1)] == m:
                result = j
            if i > 1 and size[i - 1]:
                union(i, i - 1)
            if i < n and size[i + 1]:
                union(i, i + 1)
        return result


#         n = len(arr)
#         if m == n:
#             return n
#         segments = set([(1, n)])
#         not_relevant = set()
#         for i in range(n - 1, -1, -1):
#             if arr[i] in not_relevant:
#                 continue
#             to_add = []
#             to_remove = None
#             for left, right in segments:
#                 if left <= arr[i] <= right:
#                     to_remove = (left, right)
#                     left_len = arr[i] - left
#                     right_len = right - arr[i]
#                     if left_len == m or right_len == m:
#                         return i
#                     if left_len > m:
#                         to_add.append((left, arr[i] - 1))
#                     else:
#                         for j in range(left, arr[i]):
#                             not_relevant.add(j)
#                     if right_len > m:
#                         to_add.append((arr[i] + 1, right))
#                     else:
#                         for j in range(arr[i] + 1, right + 1):
#                             not_relevant.add(j)
#                     break
#             for segment in to_add:
#                 segments.add(segment)
#             if to_remove:
#                 segments.discard(to_remove)
#             if not segments:
#                 return -1
#         return -1
