n, m = map(int, input().split())
c = list(map(int, input().split()))
a = list(map(int, input().split()))
ans = 0

a.append(0)

for i in range(n):
    if c[i] <= a[0]:
        ans += 1
        a.pop(0)

print(ans)
