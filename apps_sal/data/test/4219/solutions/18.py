from itertools import product
n = int(input())
Ev = [[] for _ in range(n)]

for i in range(n):
    A = int(input())
    for a in range(A):
        x, y = map(int, input().split())
        Ev[i].append((x - 1, y))

bit = list(product([1, 0], repeat=n))

ans = 0
for b in bit:
    for i, v in enumerate(b):
        if v == 1:
            for x, y in Ev[i]:
                if b[x] != y:
                    break
            else:
                continue
            break
    else:
        ans = max(b.count(1), ans)

print(ans)
