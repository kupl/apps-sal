n, m = list(map(int, input().split()))
a = list(map(int, input().split()))
c = [[] for _ in range(m)]
for i in range(m):
    c[i] = list(map(int, input().split()))
a.sort()
c.sort(key=lambda x: x[1], reverse=True)
ans = sum(a)
sa = 0
cnt = 0
r = c[0][0]
for i, v in enumerate(a):
    if r <= i and cnt <= m - 2:
        cnt += 1
        r += c[cnt][0]
    if r > i and v < c[cnt][1]:
        ans += abs(c[cnt][1] - v)
    else:
        break
print(ans)
