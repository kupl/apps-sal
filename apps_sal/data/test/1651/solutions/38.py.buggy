#n = int(input())
import sys
s, p = list(map(int, input().split()))
#al = list(map(int,input().split()))
#l = [list(map(int,input().split())) for i in range(n)]
#s=[list(map(int,input().split())) for i in range(n)]
i = 1
nl = []
ml = []
while i * i <= p:
    if p % i == 0:
        nl.append(i)
        ml.append(p // i)
    i += 1
for n, m in zip(nl, ml):
    if n + m == s:
        print('Yes')
        return
print('No')
