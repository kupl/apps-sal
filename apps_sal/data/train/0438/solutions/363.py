class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        from collections import defaultdict
        n = len(arr)
        parent = [i for i in range(0, n + 1)]
        group_count = defaultdict(int)
        l = [0] * n
        dd = defaultdict(int)

        def union(left, right):
            left_p = find(left)
            right_p = find(right)
            if left_p != right_p:
                parent[right_p] = left_p
                dd[group_count[right_p - 1]] -= 1
                dd[group_count[left_p - 1]] -= 1
                group_count[left_p - 1] += group_count[right_p - 1]
                group_count[right_p - 1] = 0
                dd[group_count[left_p - 1]] += 1

        def find(i):
            p = parent[i]
            if parent[p] != p:
                pp = find(p)
                parent[i] = pp
            return parent[i]

        last = -1
        for idx, num in enumerate(arr):
            l[num - 1] = 1
            group_count[num - 1] = 1
            dd[1] += 1
            if num > 1 and l[num - 2] == 1:
                union(num - 1, num)
            if num != n and l[num] == 1:
                union(num, num + 1)

            if m in dd and dd[m] > 0:
                last = idx + 1
        return last
