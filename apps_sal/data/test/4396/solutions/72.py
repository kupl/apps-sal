N = int(input())
ans = 0
for i in range(N):
    (x, u) = map(str, input().split())
    if u == 'JPY':
        ans += int(x)
    else:
        x = x.replace('.', '')
        ans += int(x) * 380000 / 10 ** 8
print(str(ans))
