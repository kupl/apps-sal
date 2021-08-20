(n, k) = map(int, input().split())
ans = 0
s = 0
while s < n:
    if s == 0:
        s += k
    else:
        s += k - 1
    ans += 1
print(ans)
