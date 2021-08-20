Q = int(input())
for _ in range(Q):
    n = int(input())
    ans = 9 * (len(str(n)) - 1)
    first = n // 10 ** (len(str(n)) - 1)
    ans += first - 1
    if n >= int(str(first) * len(str(n))):
        ans += 1
    print(ans)
