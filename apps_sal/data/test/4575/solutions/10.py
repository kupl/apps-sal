n = int(input())
(d, x) = list(map(int, input().split()))
ans = x
for i in range(n):
    t = int(input())
    ans += d // t
    if d % t != 0:
        ans += 1
print(ans)
