class Solution:

    def get_factors(self, n: int):
        factors = set()
        for factor in self.total_factors:
            if factor > n:
                break
            if n % factor == 0:
                factors.add(factor)
        for factor in factors:
            self.total_factors.remove(factor)
        return factors

    def get_prime_numbers(self, n_max: int):
        self.total_factors = [2, 3]
        for val in range(3, n_max // 2 + 2, 2):
            for i in range(3, int(val**0.5) + 2, 2):
                if val % i == 0:
                    break
                else:
                    if i >= int(val**0.5):
                        self.total_factors.append(val)

    def largestComponentSize(self, A: List[int]) -> int:
        # A.sort()
        # self.get_prime_numbers(A[-1])
        # print(self.total_factors)
        N = max(A) + 1
        nods = {d: d for d in range(N)}

        def find(x):
            root = x
            while nods[root] != root:
                root = nods[root]
            while nods[x] != root:
                parent = nods[x]
                nods[x] = root
                x = parent
            return root

        def union(x, y):
            rx, ry = find(x), find(y)
            if rx != ry:
                nods[ry] = rx

        for a in A:
            for factor in range(2, int(sqrt(a)) + 1):
                if a % factor == 0:
                    union(a, factor)
                    union(a, a // factor)

        counts = collections.defaultdict(int)
        for a in A:
            counts[find(a)] += 1
        print(counts)
        return max(counts.values())

    def largestComponentSize_slow(self, A: List[int]) -> int:
        A.sort()
        self.get_prime_numbers(A[-1])
        # print(self.total_factors)
        max_len = 0
        while len(A) > max_len:
            factors = self.get_factors(A[0])
            new_len = 1
            A.remove(A[0])
            while factors:
                factor = factors.pop()
                to_remove = []
                for i in range(len(A)):
                    if A[i] % factor == 0:
                        new_len += 1
                        rest = A[i] / factor
                        while rest % factor == 0:
                            rest /= factor
                        factors = factors | self.get_factors(rest)
                        to_remove.append(i)
                A = [A[i] for i in range(len(A)) if i not in to_remove]
            max_len = max(new_len, max_len)
        return max_len
