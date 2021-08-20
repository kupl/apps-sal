(n, s) = list(map(int, input().split()))
ans = s // n
s %= n
if s != 0:
    ans += 1
print(ans)
