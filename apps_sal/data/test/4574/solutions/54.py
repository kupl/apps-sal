from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))
D = defaultdict(int)
A.sort(reverse=True)

for i in A:
    D[i] += 1

L = []

for i, x in D.items():
    if x >= 4:
        L.append(i)
        L.append(i)
        break
    elif x >= 2:
        L.append(i)

if len(L) <= 1:
    print(0)
else:
    print(L[0] * L[1])
