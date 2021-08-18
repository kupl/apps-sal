def R(): return map(int, input().split())


f = open("input.txt", "r")
n = int(f.readline())
L = list(map(int, f.readline().split()))
'''n = int(input())
L = list(R())'''
T = []
c = 0
for i in range(n):
    T.append([c])
    if L[i] >= 0:
        c += 1
c = 0
for i in reversed(range(n)):
    T[i].append(c)
    if L[i] <= 0:
        c += 1
res = 10**9
if L[0] > 0:
    T[0][0] += 1
if L[n - 1] < 0:
    T[n - 1][1] += 1
for i in range(n):
    k = sum(T[i])
    if L[i] == 0:
        k += 1
    res = min(res, k)
open('output.txt', 'w').write(str(res))
