N = int(input())
ans = 0
for _ in range(N):
    (x, u) = input().split()
    if u == 'JPY':
        ans += int(x)
    else:
        ans += float(x) * 380000
print(ans)
