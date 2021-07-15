class Solution:
    def countVowelPermutation(self, n: int) -> int:
        a=e=i=o=u=1
        if n==0:
            return 0
        for z in range(n-1):
            a,e,i,o,u = e,a+i,a+e+o+u,i+u,a
        return (a+e+i+o+u)%1000000007
