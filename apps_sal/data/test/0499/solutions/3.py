from itertools import accumulate

n = int(input())
s = input()
D = {'R': 0, 'G': 0, 'B': 0}
for c in s:
    D[c] += 1
L = ['R', 'G', 'B']
L.sort(key=lambda c: -D[c])
if all((D[c] > 0 for c in L)) or D[L[0]] > 1 and D[L[1]] > 1:
    print('BGR')
elif D[L[1]] == 1 and D[L[0]] > 1:
    L.pop(0)
    L.sort()
    print(''.join(L))
elif D[L[1]] == 1 and D[L[0]] == 1:
    print(L[2])
else:
    print(L[0])
