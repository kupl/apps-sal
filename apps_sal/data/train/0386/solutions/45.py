class Solution:
    def countVowelPermutation(self, n: int) -> int:
        a,e,i,o,u = 1,1,1,1,1
        #store the number of each vowels
        for _ in range(1,n):
            a,e,i,o,u = e+i+u,a+i,e+o,i,i+o
        return (a+e+i+o+u)% 1000000007

