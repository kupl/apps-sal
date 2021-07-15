from math import sqrt
class Solution:
    def numSquarefulPerms(self, A: List[int]) -> int:
        return self.backtrack(A, 0, set())
    
    def isPerfect(self, num):
        return int(sqrt(num))**2 == num
        
    def backtrack(self, permutation, j, seen):
        permutation_tuple = (j,) + tuple(permutation)
        if permutation_tuple in seen: return 0
        seen.add(permutation_tuple)
        if j == len(permutation):
            return 1
        total = 0
        for i in range(j, len(permutation)):
            self.swap(permutation, i, j)
            if j == 0 or self.isPerfect(permutation[j] + permutation[j-1]):
                total += self.backtrack(permutation, j+1, seen)
            self.swap(permutation, i, j)
        return total
    
    def swap(self, array, i, j):
        array[i], array[j] = array[j], array[i]

