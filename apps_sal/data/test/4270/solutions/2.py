n = int(input())
v = list(map(int, input().split()))
v.sort()
x = v[0]
if n > 2:
    for i in range(1, n):
        x += v[i] * 2 ** (i - 1)
    ans = x / 2 ** (n - 1)
    print(ans)
else:
    print((x + v[1]) / 2)
