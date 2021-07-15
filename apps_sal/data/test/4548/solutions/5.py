lst = input().split()
N = int(lst[0])
M = int(lst[1])
X = int(lst[2])
L = input().split()

cost_0 = 0
for n in L:
   if 0 < int(n) < X:
      cost_0 += 1
   elif X < int(n):
      break

cost_N = 0
for n in L:
   if X < int(n) < N:
      cost_N += 1

print(min([cost_0, cost_N]))
