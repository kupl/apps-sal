class Solution:

    def largestComponentSize(self, A: List[int]) -> int:
        count = [1 for _ in A]
        parent = [i for i in range(len(A))]
        
        def find_it(index):
            while index != parent[index]:
                index = parent[index]
            return index

        def union_it(index1, index2):
            p, q = find_it(index1), find_it(index2)
            if p == q:
                return
            if count[p] < count[q]:
                p, q = q, p
            count[p] += count[q]
            parent[q] = p


        top = floor(sqrt(max(A)))
        is_prime = [True for _ in range(1 + top)]
        is_prime[0], is_prime[1] = False, False
        for p in range(2, len(is_prime)):
            if not is_prime[p]:
                continue
            k = -1
            for i in range(len(A)):
                if A[i] % p:
                    continue
                while (A[i] % p) == 0:
                    A[i] //= p
                if k < 0:
                    k = i
                else:
                    union_it(k,i)
            p1 = 2 * p
            while p1 <= top:
                is_prime[p1] = False
                p1 += p

        AA = [(n, i) for i, n in enumerate(A) if n > 1]
        AA.sort()
        for index in range(1,len(AA)):
            if AA[index-1][0] == AA[index][0]:
                union_it(AA[index-1][1], AA[index][1])
        return max(count)        
