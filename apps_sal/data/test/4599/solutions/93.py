n = int(input())
x = [int(i) for i in input().split()]
xx = sorted(x)
ans = 0
aaa = 0
if n % 2 == 0:
    for i in range(n // 2):
        ans += xx[i * 2 + 1] - xx[i * 2]
    print(ans)
else:
    for i in range(n // 2):
        ans += xx[i * 2 + 1] - xx[i * 2]
    aaa = xx[n - 1] - ans
    print(aaa)
