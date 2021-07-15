from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))
D = defaultdict(int)

for i in A:
  D[i] += 1

L1 = [0, 0]
L2 = [0]

for i, x in D.items():
  if x >= 4:
    L2.append(i)
  if x >= 2:
    L1.append(i)

L1.sort(reverse=True)
L2.sort(reverse=True)

print(max(L1[0]*L1[1], L2[0]**2))
