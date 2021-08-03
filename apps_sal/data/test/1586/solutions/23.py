n = int(input())

ans = 0
if n % 2 == 0:
    for i in range(1, 36):
        k = 5**i * 2
        ans += n // k
    print(ans)
else:
    print(ans)
