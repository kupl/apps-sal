
n, m = list(map(int, input().split()))

ans = 0
cc = m // 2
if n >= cc:
    ans = cc
else:
    ans = (n + cc) // 2
print(ans)
