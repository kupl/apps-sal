n = int(input())
a = [int(i) for i in input().split()]
s = 0
for i in a:
    s += i
m = s // n
ans = 0
for i in range(n - 1):
    ans += abs(m - a[i])
    if a[i] < m:
        a[i + 1] -= m - a[i]
    else:
        a[i + 1] += a[i] - m
print(ans)
