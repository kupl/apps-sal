n, m = map(int, input().split())
x = [0] * n
s = 0
for i in range(m):
    a, b = map(int, input().split())
    if a == 1:
        if x[b - 1] == 0:
            x[b - 1] = 1
        elif x[b - 1] == -1:
            s += 1
    elif b == n:
        if x[a - 1] == 0:
            x[a - 1] = -1
        elif x[a - 1] == 1:
            s += 1
if s > 0:
    print("POSSIBLE")
else:
    print("IMPOSSIBLE")
