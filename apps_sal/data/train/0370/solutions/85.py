from typing import List, Set, Tuple

def prime_factors(n: int) -> Set[int]:
    f = set()
    i = 1
    while n % 2 == 0 and n:
        f.add(2)
        n //= 2
    while n % 3 == 0 and n:
        f.add(3)
        n //= 3
    root = int(n ** 0.5) + 1
    while True and n:
        a, b = 6 * i + 1, 6 * i - 1
        while n % a == 0:
            n //= a
            f.add(a)
        while n % b == 0:
            n //= b
            f.add(b)
        if a > root:
            break
        i += 1
    if n > 1:
        f.add(n)
    return f

class Solution:
    def largestComponentSize(self, A: List[int]) -> int:
        A.sort(reverse=True)
        islands: List[Tuple[Set[int], int]] = []
        primes: Set[int] = set()
        for n in A:
            factors = prime_factors(n)
            first_merged = None
            to_delete: Set[int] = set()
            for i, (g, v) in enumerate(islands):
                if factors.isdisjoint(g):
                    continue
                if first_merged is None:
                    g.update(factors)
                    islands[i] = (g, v + 1)
                    first_merged = i
                else:
                    gf, vf = islands[first_merged]
                    gf.update(g)
                    islands[first_merged] = (gf, vf + v)
                    to_delete.add(i)
            primes_inside = factors & primes
            if primes_inside:
                if first_merged is None:
                    new_v = len(primes_inside) + 1
                    islands.append((factors, new_v))
                else:
                    gf, vf = islands[first_merged]
                    islands[first_merged] = (gf, vf + len(primes_inside))
                primes.difference_update(primes_inside)
            elif first_merged is None:
                if n in factors:
                    primes.add(n)
                else:
                    islands.append((factors, 1))
            islands = [g for i, g in enumerate(islands) if i not in to_delete]
        return max(v for g, v in islands)
            
            
            
        

