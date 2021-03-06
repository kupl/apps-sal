from collections import defaultdict


class Solution:

    def largestComponentSize(self, A: List[int]) -> int:
        small_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]
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
            for p in small_primes:
                if x % p == 0:
                    root_id = findRoot(p) if root_id == 0 else mergeRoot(root_id, p)
                    while x % p == 0:
                        x //= p
            if x != 1:
                root_id = findRoot(x) if root_id == 0 else mergeRoot(root_id, x)
            label[root_id] -= 1
        return -min(label.values())
