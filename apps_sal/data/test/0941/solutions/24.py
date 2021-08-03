b, k = [int(x) for x in input().split()]

L = [int(x) for x in input().split()]

t = 0
for i in range(0, len(L) - 1):
    t += L[i]

t *= b % 2
t += L[-1]
if t % 2 == 0:
    print('even')
else:
    print('odd')
