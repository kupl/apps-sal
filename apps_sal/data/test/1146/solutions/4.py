n, m = [int(x) for x in input().split()]
b = [False] * m
for _ in range(n):
    for y in [int(x) for x in input().split()][1:]:
        b[y-1] = True

if all(b):
    print("YES")
else:
    print("NO")

