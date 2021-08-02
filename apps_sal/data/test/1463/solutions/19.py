from itertools import *
n = int(input())
f = [list(map(int, input().split())) for _ in range(n)]
for i, j in product(list(range(n)), list(range(n))):
    x = f[i][j]
    if x == 1:
        continue
    if not any(a + b == x for a, b in product(chain(f[i][:j], f[i][j + 1:]), (f[k][j] for k in chain(list(range(i)), list(range(i + 1, n)))))):
        print("No")
        return
print("Yes")
