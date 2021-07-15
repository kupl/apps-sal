3
#coding: utf-8

N, H = (int(x) for x in input().split())

A = []
B = []
for i in range(N):
    a, b = (int(x) for x in input().split())
    A.append(a)
    B.append(b)

A.sort(reverse=True)
B.sort(reverse=True)

ret = 0
AMax=A[0]
for b in B:
    if b < AMax or H <= 0:
        break
    H -= b
    ret += 1

if (H > 0):
    ret += H // AMax
    if H % AMax != 0:
        ret += 1
print(ret)
