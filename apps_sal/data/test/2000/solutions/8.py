"""
Created on Jul 29, 2016

@author: Md. Rezwanul Haque
"""
"'\nn = int(input())\nL = list(map(int,input().split()))\ncnt  = 0\nfor i in range(n):\n    for j in range(i,n):\n        if i<j and (L[i]+L[j])%2 == 0:\n            for k in range(31):\n                if pow(2, k) == L[i]+L[j]:\n                    cnt+=1\n                    #print(i,j)\n                    break\n            \n            #cnt+=1\nprint(cnt)"
n = int(input())
d = {}
for i in input().split():
    if int(i) in d:
        d[int(i)] += 1
    else:
        d[int(i)] = 1
L = []
for i in range(1, 33):
    L.append(2 ** i)
ans = 0
for i in d:
    for j in L:
        if j - i in d:
            if j - i != i:
                ans += d[j - i] * d[i]
            else:
                ans += (d[i] - 1) * d[i]
print(ans // 2)
