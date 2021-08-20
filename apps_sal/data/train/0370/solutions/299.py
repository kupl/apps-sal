from collections import defaultdict


class Solution:

    def largestComponentSize(self, A: List[int]) -> int:
        small_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317]
        label = defaultdict(int)

        def findRoot(key):
            if label[key] > 0:
                label[key] = findRoot(label[key])
                return label[key]
            else:
                return key

        def mergeRoot(k1, k2):
            (r1, r2) = (findRoot(k1), findRoot(k2))
            if r1 != r2:
                (r1, r2) = (min(r1, r2), max(r1, r2))
                label[r1] += label[r2]
                label[r2] = r1
            return r1
        for x in A:
            root_id = 0
            t = sqrt(x) + 1
            for p in small_primes:
                if p > t:
                    break
                elif x % p == 0:
                    root_id = findRoot(p) if root_id == 0 else mergeRoot(root_id, p)
                    while x % p == 0:
                        x //= p
            if x != 1:
                root_id = findRoot(x) if root_id == 0 else mergeRoot(root_id, x)
            label[root_id] -= 1
        return -min(label.values())
