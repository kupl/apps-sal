t = int(input())
for q in range(t):
    n = int(input())
    ans = 0
    k = 1
    while k <= (n + 1):
        ans += n // k
        k *= 2
    print(ans)
