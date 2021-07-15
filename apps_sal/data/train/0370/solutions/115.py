import numpy as np
class Solution:
    def largestComponentSize(self, A: List[int]) -> int:
        # second attempt, going factor-wise using disjoint set structure
        # A = np.array(A)
        # start with parent pointing to themselves
        parents = np.arange(len(A))
        
        # count of each node starting at 1 (itself)
        counts = np.ones_like(parents)
        
        def find(i):
            if parents[i] == i:
                return i
            else:
                return find(parents[i])
        
        def combine(i, j):
            pi = find(i)
            pj = find(j)
            
            # only do something if not already linked
            if pi != pj:
                # merge under the biggest root
                if counts[pi] > counts[pj]:
                    parents[pj] = pi
                    counts[pi] += counts[pj]
                else:
                    parents[pi] = pj
                    counts[pj] += counts[pi]
        
        max_prime = int(np.floor(np.sqrt(max(A))))+1
        # max_prime = max(A)
        
#         def get_primes(value: int) -> List[int]:
#             ret = []
#             sieve = [True]*(value+1)
#             for p in range(2, value+1):
#                 if sieve[p]:
#                     ret.append(p)
#                     for k in range(p, value+1, p):
#                         sieve[k] = False
#             return ret
        
#         primes = get_primes(max_prime)
        
#         for prime in primes:
#             match = -1
#             for i in range(len(A)):
#                 if A[i] % prime == 0:
#                     while A[i] % prime == 0:
#                         A[i] = A[i] // prime  # keep factoring out
#                     if match != -1:
#                         # do the merge
#                         combine(match, i)
#                     else:
#                         match = i # first one found, merge from now on
        
        
        sieve = [True]*(max_prime+1)
        for prime in range(2, max_prime+1):
            if sieve[prime]:
                match = -1
                for i in range(len(A)):
                    if A[i] % prime == 0:
                        while A[i] % prime == 0:
                            A[i] = A[i] // prime  # keep factoring out
                        if match != -1:
                            # do the merge
                            combine(match, i)
                        else:
                            match = i # first one found, merge from now on
                for k in range(prime, max_prime+1, prime):
                    sieve[k] = False
        
        # leftover values of A are now higher primes (or 1)
        # if any match, they need to be merged
        inds = np.argsort(A)
        
        # print(A)
        # print(inds)
        # print(A[inds])
        for i in range(1,len(A)):
            if (A[inds[i]] != 1) and (A[inds[i-1]] == A[inds[i]]):
                combine(inds[i-1], inds[i])
        
        return np.max(counts)
        
        # first attempt
        # TLE at 78/100
#         # note: a value of 1 cannot be connected to anything
#         # can clump things together based on factors
        
#         def get_factors(value: int) -> List[int]:
#             if value == 1:
#                 return set()
#             # ret = [value]
#             ret = set([value])
            
#             # if value % 2 == 0:
#             #     ret.append(2)
#             #     ret.append(value // 2)
            
#             for i in range(2, int(np.floor(np.sqrt(value)))+1):
#                 if value % i == 0:
#                     ret.add(i)
#                     ret.add(value // i)
#                     # ret.append(i)
#                     # ret.append(value // i)
            
#             return ret
#             # return set(ret)
        
        
#         # def get_primes(value: int) -> List[int]:
#         #     ret = []
#         #     sieve = [True]*(value+1)
#         #     for p in range(2, value+1):
#         #         if sieve[p]:
#         #             ret.append(p)
#         #             for k in range(p, value+1, p):
#         #                 sieve[k] = False
#         #     return ret
        
#         # trying more efficient get_primes implementation
#         # def get_primes(n: int) -> List[int]:
#         #     # modified from
#         #     # https://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
#         #     sieve = np.ones(n//3 + (n%6==2), dtype=np.bool)
#         #     sieve[0] = False
#         #     for i in range(int(n**0.5)//3+1):
#         #         if sieve[i]:
#         #             k=3*i+1|1
#         #             sieve[      ((k*k)//3)      ::2*k] = False
#         #             sieve[(k*k+4*k-2*k*(i&1))//3::2*k] = False
#         #     return np.r_[2,3,((3*np.nonzero(sieve)[0]+1)|1)]
        
#         def get_primes(n: int) -> List[int]:
#             sieve = [True] * n
#             for i in range(3,int(n**0.5)+1,2):
#                 if sieve[i]:
#                     sieve[i*i::2*i]=[False]*((n-i*i-1)//(2*i)+1)
#             return [2] + [i for i in range(3,n,2) if sieve[i]]
        
#         primes = get_primes(int(np.floor(np.sqrt(max(A))))+1)
#         # primes = get_primes(max(A))
        
#         def get_factors(value: int) -> List[int]:
#             ret = set([value])
#             for prime in primes:
#                 if prime > value:
#                     return ret
#                 else:
#                     if value % prime == 0:
#                         ret.add(prime)
#                         while value % prime == 0:
#                             value /= prime
                        
#                         # ret.add(value//prime)
#                         # value /= prime  # factor out prime for efficiency
#                         # while value % prime == 0:
#                         #     ret.add(value//prime)
#                         #     value /= prime
                        
#                         # if value // prime in primes:
#                         # ret.add(value//prime)
#                         # value /= prime  # factor out prime for efficiency
#                         # if value > 1:
#                         #     ret.add(value)
#                         # else:
#                         #     break
#                         # while value % prime == 0:
#                         #     # if value // prime in primes:
#                         #     # ret.add(value//prime)
#                         #     value /= prime
#                         #     if value > 1:
#                         #         ret.add(value)
#                         #     else:
#                         #         break
#             if value > 1:
#                 ret.add(value)
#             return ret
        
#         clusters = []
#         sizes = []
        
#         for value in A:
#             factors = get_factors(value)
#             # check cluster matches, all that get matched get merged
#             matches = []
#             for j, cluster in enumerate(clusters):
#                 if not cluster.isdisjoint(factors):
#                     matches.append(j)
#             # if not in any cluster, make a new cluster
#             if len(matches) == 0:
#                 clusters.append(factors)
#                 sizes.append(1)
#             elif len(matches) == 1:
#                 clusters[matches[0]].update(factors)
#                 sizes[matches[0]] += 1
#             else:
#                 base = matches[0]
#                 # iterate backwards so they can be deleted safely
#                 for match in matches[-1:0:-1]:
#                     clusters[base].update(clusters[match])
#                     sizes[base] += sizes[match]
#                     del clusters[match]
#                     del sizes[match]
                
#                 # add the new factors
#                 clusters[base].update(factors)
#                 sizes[base] += 1      

#         return max(sizes)
            
        

