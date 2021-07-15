t = int(input())
for _ in range(t):
    n, m = list(map(int, input().split()))
    ans = 0
    for B in range(1, 11):
        b = 10 ** B - 1
        if b > m:
            break
        ans += n
    print(ans)

