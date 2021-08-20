class Solution:

    def largestComponentSize(self, A: List[int]) -> int:
        n = len(A)
        if n < 2:
            return n
        A = set(A)
        if 1 in A:
            A.remove(1)
        if len(A) == 0:
            return 1

        def list_primes(m):
            p = [True] * (m + 1)
            for i in range(2, m + 1):
                if p[i]:
                    for j in range(2 * i, m + 1, i):
                        p[j] = False
            return [i for i in range(2, m + 1) if p[i]]

        def find_prime_factors(x, prime_list, prime_set):
            if x in prime_set:
                return [x]
            prime_factors = []
            for prime_num in prime_list:
                if prime_num * prime_num > x:
                    break
                if x % prime_num == 0:
                    prime_factors.append(prime_num)
                    while x % prime_num == 0:
                        x //= prime_num
            if x != 1:
                prime_factors.append(x)
            return prime_factors
        prime_list = list_primes(max(A))
        prime_set = set(prime_list)
        d = {x: find_prime_factors(x, prime_list, prime_set) for x in A}
        all_factors = set()
        for x in A:
            for f in d[x]:
                all_factors.add(f)
        find_dict = {f: f for f in all_factors}
        sink_size = {f: 1 for f in all_factors}

        def find(f):
            if find_dict[f] != f:
                find_dict[f] = find(find_dict[f])
            return find_dict[f]

        def union(fi, fj):
            sink_i = find(fi)
            sink_j = find(fj)
            if sink_i == sink_j:
                return
            if sink_size[sink_i] > sink_size[sink_j]:
                find_dict[sink_j] = sink_i
                sink_size[sink_i] += sink_size[sink_j]
            else:
                find_dict[sink_i] = sink_j
                sink_size[sink_j] += sink_size[sink_i]

        def union_hyperedge(hyperedge):
            for i in range(1, len(hyperedge)):
                union(hyperedge[i], hyperedge[0])
        for x in A:
            union_hyperedge(d[x])
        sinks = set()
        for f in all_factors:
            sinks.add(find(f))
        count = {sink: 0 for sink in sinks}
        for x in A:
            count[find(d[x][0])] += 1
        return max(count.values())
