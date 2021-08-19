class DisjointSet:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0 for i in range(n)]

    def GetParent(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.GetParent(self.parent[i])

        return self.parent[i]

    def Union(self, i, j):
        i_idx = self.GetParent(i)
        j_idx = self.GetParent(j)

        if j_idx == i_idx:
            return

        if self.rank[i_idx] > self.rank[j_idx]:
            self.parent[j_idx] = i_idx
        else:
            if self.rank[i_idx] == self.rank[j_idx]:
                self.rank[j_idx] += 1

            self.parent[i_idx] = j_idx


class Solution:
    def largestComponentSize(self, A: List[int]) -> int:
        def prime_set(n):
            for i in range(2, math.floor(math.sqrt(n)) + 1):
                if n % i == 0:
                    return prime_set(n // i) | set([i])

            return set([n])

        ds = DisjointSet(len(A))

        primes = {}

        for i in range(len(A)):
            curr_prime_set = prime_set(A[i])

            for prime in curr_prime_set:
                primes.setdefault(prime, [])
                primes[prime].append(i)

        for key in primes:
            for i in range(len(primes[key]) - 1):
                ds.Union(primes[key][i], primes[key][i + 1])

        set_counter = {}

        for i in range(len(A)):
            set_counter.setdefault(ds.GetParent(i), 0)
            set_counter[ds.GetParent(i)] += 1

        # print(set_counter)
        return max(set_counter.values())


#     def largestComponentSize(self, A: List[int]) -> int:
#         def gcd(a, b):
#             nonlocal gcd_hash
#             if (a, b) in gcd_hash:
#                 return gcd_hash[(a, b)]

#             if b == 0:
#                 return a

#             if a >= b:
#                 return gcd(b, a % b)
#             else:
#                 return gcd(a, b % a)


#         def Explore(u, adj_list, visited):
#             visited[u] = 1

#             for v in adj_list[u]:
#                 if not visited[v]:
#                     nonlocal cc_length
#                     cc_length += 1
#                     Explore(v, adj_list, visited)


#         gcd_hash = {}
#         V = len(A)
#         adj_list = [[] for _ in range(V)]

#         for i in range(len(A)):
#             for j in range(i + 1, V):
#                 curr_gcd = gcd(A[i], A[j])
#                 gcd_hash[(A[i], A[j])] = curr_gcd
#                 gcd_hash[(A[j], A[i])] = curr_gcd

#                 if curr_gcd > 1:
#                     adj_list[i].append(j)
#                     adj_list[j].append(i)

#         # print(adj_list)

#         visited = [0 for _ in range(V)]
#         max_cc_length = 0
#         cc_num = 0
#         cc_length = 1

#         for i in range(V):
#             if not visited[i]:
#                 Explore(i, adj_list, visited)
#                 cc_num += 1

#                 if cc_length > max_cc_length:
#                     max_cc_length = cc_length

#                 cc_length = 1

#         # print(cc_num)
#         # print(max_cc_length)

#         return max_cc_length
