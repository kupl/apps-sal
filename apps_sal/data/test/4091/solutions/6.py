(n, k) = map(int, input().split())
a = list(map(int, input().split()))
b = [0] * 3000
for i in range(n):
    a[i] = (i, a[i])
a.sort(key=lambda x: x[1], reverse=True)
for i in range(k):
    b[a[i][0]] = 1
cur = 0
ans = []
total = 0
addtolast = 0
a.sort(key=lambda x: x[0])
for i in range(n):
    if b[i] == 1:
        total += a[i][1]
        ans.append(i - cur + 1)
        addtolast = n - i - 1
        cur = i + 1
ans[-1] += addtolast
print(total)
print(*ans)
