n = int(input())
a = list(map(int, input().split()))
c = [0] * 100000
for i in range(n):
    c[a[i] - 1] += 1
s = []
for i in range(n):
    if c[i] == 0:
        s.append(i + 1)
if not s:
    print(*a)
    return
ans = a[:]
x = 0
for i in range(n):
    if c[a[i] - 1] > 1 or a[i] > n:
        c[a[i] - 1] -= 1
        ans[i] = s[x]
        x += 1
print(*ans)
