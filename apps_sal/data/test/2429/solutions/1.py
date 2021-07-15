t = int(input())
for i in range(t):
    n = int(input())
    ans = 0
    for j in range(1, n // 2 + 1):
        ans += 2**j
    print(ans)
