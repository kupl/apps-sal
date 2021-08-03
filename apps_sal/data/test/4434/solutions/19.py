t = int(input())
for i in range(t):
    n = int(input())
    ans = (n // 2) * n**2
    for j in range(n // 2):
        ans -= (2 * j + 1)**2
    print(ans)
