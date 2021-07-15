n, m = list(map(int, input().split()))
d = []
nsum = 0
for _ in range(n):
    a, b = list(map(int, input().split()))
    d.append(a-b)
    nsum += a
d.sort(reverse = True)
ans = 0
for i in range(n):
    if nsum <= m:
        print(ans)
        return
    else:
        nsum -= d[i]
        ans += 1
print(-1 if nsum > m else ans)

