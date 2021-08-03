class Solution:
    def __init__(self):
        self.prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317]

    def largestComponentSize(self, A: List[int]) -> int:
        n = len(A)
        factors_2_nodes = dict()
        B = [[] for i in range(0, n)]
        for i in range(0, n):
            num = A[i]
            found_factor = True
            while num > 1 and found_factor:
                found_factor = False
                limit = int(sqrt(num + 1))
                for f in self.prime:
                    if f > limit:
                        break
                    if num % f == 0:
                        if f not in B[i]:
                            B[i].append(f)
                            if f in factors_2_nodes:
                                factors_2_nodes[f].append(i)
                            else:
                                factors_2_nodes[f] = [i]
                        num //= f
                        found_factor = True
                        break
                if not found_factor and num not in B[i]:
                    B[i].append(num)
                    if num in factors_2_nodes:
                        factors_2_nodes[num].append(i)
                    else:
                        factors_2_nodes[num] = [i]
        v = [False] * n
        m = 0
        for i in range(0, n):
            if v[i]:
                continue
            queue = [i]
            c = 0
            while queue:
                q = queue.pop()
                if v[q]:
                    continue
                v[q] = True
                c += 1
                for f in B[q]:
                    for node in factors_2_nodes[f]:
                        if not v[node]:
                            queue.append(node)
                    factors_2_nodes[f] = []
            if c > m:
                m = c
        return m
