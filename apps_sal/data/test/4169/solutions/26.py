
n, m = map(int, input().split())
s = []
ans = 0
for i in range(n):
    a, b = map(int, input().split())
    s.append([a, b])
s.sort()
for i in s:
    if m < i[1]:
        ans += m * i[0]
        break
    else:
        ans += i[0] * i[1]
        m -= i[1]
print(ans)
