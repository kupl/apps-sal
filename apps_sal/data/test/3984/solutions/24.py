"""
NTC here
"""
from sys import setcheckinterval, stdin, setrecursionlimit
setcheckinterval(1000)
setrecursionlimit(10**7)
 
# print("Case #{}: {} {}".format(i, n + m, n * m))
 
 
def iin(): return int(stdin.readline())
 
 
def lin(): return list(map(int, stdin.readline().split()))

s=input()
a=[]
i=0
l=len(s)
least='z'
while i<l:
    x=s[i]
    least=min(x,least)
    while i<l and s[i]==x:
        if least<x:
            a.append('Ann')
        else:
            a.append('Mike')
        i+=1
print(*a,sep='\n')

