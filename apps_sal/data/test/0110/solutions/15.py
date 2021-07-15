n = int(input())
a = list(map(int, input().split()))
if n%2 == 0:
    for i in range(n):
        if a[i] >= 0:
            a[i] = -1 * a[i] - 1
else:
    b = []
    for ai in a:
        b.append(-1 * ai - 1 if ai < 0 else ai)
    m = max(b)
    done = False
    for i in range(n):
        if not done and b[i] == m:
            a[i] = b[i]
            done = True
        else:
            a[i] = -1 * b[i] - 1
print(*a, sep=' ')

