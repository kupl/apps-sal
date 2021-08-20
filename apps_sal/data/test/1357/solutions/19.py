(n, m) = map(int, input().split())
a = (1,) + tuple(map(int, input().split()))
ans = 0
for i in range(1, len(a)):
    ans += (a[i] - a[i - 1] + n) % n
print(ans)
