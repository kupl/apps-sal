'''
Created on Jul 29, 2016

@author: Md. Rezwanul Haque
'''
''''
n = int(input())
L = list(map(int,input().split()))
cnt  = 0
for i in range(n):
    for j in range(i,n):
        if i<j and (L[i]+L[j])%2 == 0:
            for k in range(31):
                if pow(2, k) == L[i]+L[j]:
                    cnt+=1
                    break
            
print(cnt)'''


n = int(input())

d = {}

for i in input().split():
    if int(i) in d:
        d[int(i)] += 1
    else:
        d[int(i)] = 1

L = []

for i in range(1, 33):
    L.append(2**i)

ans = 0

for i in d:
    for j in L:
        if j - i in d:
            if j - i != i:
                ans += d[j - i] * d[i]
            else:
                ans += (d[i] - 1) * (d[i])
print(ans // 2)
