class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        res = -1
        mem = {}
        count = collections.Counter()
        group_size = {}
        def find(k):
            if mem[k] != k:
                mem[k] = find(mem[k])
            return mem[k]

        def union(n1, n2):
            f1, f2 = find(n1), find(n2)
            if f1 != f2:
                count[group_size[f1]] -= 1
                count[group_size[f2]] -= 1
                group_size[f1] += group_size[f2]
                count[group_size[f1]] += 1
                mem[f2] = f1

        for idx, v in enumerate(arr, 1):
            mem[v] = v
            group_size[v] = 1
            count[1] += 1
            left = v - 1 if v - 1 in mem else v
            right = v + 1 if v + 1 in mem else v
            union(left, v)
            union(v, right)
            if count[m] > 0:
                res = idx
        return res
