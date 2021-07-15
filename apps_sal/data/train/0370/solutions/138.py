class Solution:
    def largestComponentSize(self, A: List[int]) -> int:
        import math
        n = len(A)
        G = collections.defaultdict(set)
        def get_prime_list(target):
            dest = int(math.sqrt(target))
            target_list = list(range(2, target + 1))
            prime_list = []

            while True:
                num_min = min(target_list)
                if num_min >= dest:
                    prime_list.extend(target_list)
                    break
                prime_list.append(num_min)


                i = 0

                while True:
                    if i >= len(target_list):
                        break
                    elif target_list[i] % num_min == 0:
                        target_list.pop(i)
                    i += 1

            return prime_list
        def primes_set(n):
            for i in range(2, int(math.sqrt(n))+1):
                if n % i == 0:
                    return primes_set(n//i) | set([i])
            return set([n])
        #primes = get_prime_list(min(100000,max(A)))
        #primes = primes_set
        def find(x):
            if p[x] != x:
                p[x] = find(p[x])
            return p[x]
        def union(x,y):
            x = find(x)
            y = find(y)
            p[y] = x
            
        for a in A:
            G[a] = set()
        pdic = collections.defaultdict(set)
        p = list(range(len(A)))
        for idx,i in enumerate(A):
            for j in primes_set(i):
                    pdic[j].add(idx)
        for k,v in  list(pdic.items()):
            n = len(v)
            tmp = list(v)
            for i in range(n-1):
                union(tmp[i],tmp[i+1])  
        tmp = []
        for i in range(len(A)):
            tmp.append(find(i))
        c = Counter(tmp)
        return max(c.values())
                    

