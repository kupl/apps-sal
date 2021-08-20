class Solution:

    def findLatestStep(self, arr: List[int], m: int) -> int:
        n = len(arr)
        if m == n:
            return n
        groups = defaultdict(set)
        parents = [i for i in range(n)]
        size = [0] * n

        def find(node):
            if parents[node] == node:
                return node
            parent = find(parents[node])
            return parent

        def union(a, b):
            para = find(a)
            parb = find(b)
            if para != parb:
                groups[parb].update(groups[para])
                groups.pop(para)
                parents[para] = parb

        def get_size(a):
            parent = find(parents[a])
            return len(groups[parent])

        def update(i):
            check = get_size(i)
            sizes[check] -= 1
            if sizes[check] == 0:
                sizes.pop(check)
        arr = [i - 1 for i in arr]
        step = 0
        ans = -1
        sizes = Counter()
        for i in arr:
            step += 1
            size[i] += 1
            groups[i].add(i)
            sizes[1] += 1
            if i - 1 >= 0 and i + 1 < n and size[i - 1] and size[i + 1]:
                update(i - 1)
                update(i + 1)
                union(i, i - 1)
                union(i + 1, i - 1)
                sizes[1] -= 1
                if sizes[1] == 0:
                    sizes.pop(1)
                new_size = get_size(i - 1)
                sizes[new_size] += 1
            elif i - 1 >= 0 and size[i - 1]:
                update(i - 1)
                union(i, i - 1)
                sizes[1] -= 1
                if sizes[1] == 0:
                    sizes.pop(1)
                new_size = get_size(i - 1)
                sizes[new_size] += 1
            elif i + 1 < n and size[i + 1]:
                update(i + 1)
                union(i, i + 1)
                sizes[1] -= 1
                if sizes[1] == 0:
                    sizes.pop(1)
                new_size = get_size(i + 1)
                sizes[new_size] += 1
            if m in sizes:
                ans = step
        return ans
