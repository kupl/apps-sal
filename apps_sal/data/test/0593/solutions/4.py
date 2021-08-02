n, m = list(map(int, input().split()))
p = [0] * n
for i in range(m):
    a = list(map(int, input().split()))
    q = max(a)
    for t in range(n):
        if a[t] == q:
            r = t
            break
    p[t] += 1
q = max(p)
for i in range(n):
    if p[i] == q:
        print(i + 1)
        break
