class Solution:

    def findLatestStep(self, arr: List[int], m: int) -> int:
        (n, res) = (len(arr), -1)
        if m == n:
            return n
        if m == 1 and n == 1:
            return 1
        (string, size, root) = ([0] * n, [1] * n, [-1] * n)

        def find(a):
            if root[a] != a:
                root[a] = find(root[a])
            return root[a]

        def union(a, b):
            (find_a, find_b) = (find(a), find(b))
            root[find_a] = find_b
            size[find_b] += size[find_a]
        for step in range(n):
            idx = arr[step] - 1
            string[idx] = 1
            root[idx] = idx
            if idx - 1 >= 0 and string[idx - 1] == 1:
                if m == size[find(idx - 1)]:
                    res = step
            if idx + 1 < n and string[idx + 1] == 1:
                if m == size[find(idx + 1)]:
                    res = step
            if idx - 1 >= 0 and string[idx - 1] == 1:
                union(idx - 1, idx)
            if idx + 1 < n and string[idx + 1] == 1:
                union(idx + 1, idx)
        return res


'\n[3,5,1,2,4]\n1\n[3,1,5,4,2]\n2\n[1]\n1\n[2, 1]\n2\n[3,2,5,6,10,8,9,4,1,7]\n3\n[4,3,2,1]\n1\n'
