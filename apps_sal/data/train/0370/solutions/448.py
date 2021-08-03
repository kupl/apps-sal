from collections import defaultdict, deque


class Solution:
    def largestComponentSize(self, A: List[int]) -> int:
        primes = []
        i = 2
        while i ** 2 <= 100000:
            flg = True
            for p in primes:
                if i % p == 0:
                    flg = False
                    break
            if flg:
                primes.append(i)
            i += 1

        d, primeToNode = defaultdict(set), defaultdict(set)
        for i, x in enumerate(A):
            for p in primes:
                if x % p == 0:
                    while x % p == 0:
                        x //= p
                    d[A[i]].add(p)
                    primeToNode[p].add(A[i])
            if x > 1:
                d[A[i]].add(x)
                primeToNode[x].add(A[i])
        visited, visited_prime = set(), set()
        ans = 0
        for x in A:
            if x not in visited:
                q = deque([x])
                visited.add(x)
                tmp = {x}
                while len(q) > 0:
                    cur = q.popleft()
                    for p in d[cur]:
                        if p not in visited_prime:
                            for adj in primeToNode[p]:
                                if adj not in visited:
                                    visited.add(adj)
                                    tmp.add(adj)
                                    q.append(adj)
                            visited_prime.add(p)
                ans = max(ans, len(tmp))

        return ans
