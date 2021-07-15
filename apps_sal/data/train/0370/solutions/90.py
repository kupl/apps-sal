class UnionFind:
    def __init__(self, num: int):
        self.parents = [i for i in range(num)]
        self.size = [1] * num
        self.max = 1
    
    def find(self, number: int) -> int:
        if self.parents[number] != number:
            self.parents[number] = self.find(self.parents[number])
        return self.parents[number]
    
    def merge(self, x: int, other: int):
        parentX = self.find(x)
        parentOther = self.find(other)
        
        if parentX != parentOther:
            size_x, size_y = self.parents[parentX], self.parents[parentOther]

            self.parents[parentX] = parentOther
            self.size[parentOther] += self.size[parentX]

            if self.size[parentOther] > self.max:
                self.max = self.size[parentOther]
            

class Solution:
    def primesBefore(self, value: int) -> List[int]:
        candidates = [True] * (value + 1)
        primeList = []
        
        for i in range(2, value + 1):
            if not candidates[i]:
                continue
            primeList.append(i)
            for j in range(i, value + 1, i):
                candidates[j] = False
        
        return primeList
        
    def largestComponentSize(self, A: List[int]) -> int:
        union_find = UnionFind(len(A))
        cache = {}
        primes = self.primesBefore(max(A))
        primeset = set(primes)
        
        for index, value in enumerate(A):
            svalue = value
            primeIndex = 0
            
            while svalue not in primeset and primes[primeIndex] <= svalue:
                j = primes[primeIndex]
                if svalue % j != 0:
                    primeIndex += 1
                    continue

                if j not in cache:
                    cache[j] = index
                else:
                    union_find.merge(index, cache[j])
                if value // j not in cache:
                    cache[value // j] = index
                else:
                    union_find.merge(index, cache[value // j])
                
                while svalue % j == 0:
                    svalue //= j
                primeIndex += 1
            
            if svalue == 1:
                continue
            if svalue not in cache:
                cache[svalue] = index
            else:
                union_find.merge(index, cache[svalue])
        
        return union_find.max
        
        
        

