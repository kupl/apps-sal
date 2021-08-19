n = int(input())
(d, x) = list(map(int, input().split()))
ans = x
for _ in range(n):
    a = int(input())
    ans += (d + a - 1) // a
print(ans)
