N, K = list(map(int, input().split()))
A = list(map(int, input().split()))
Asum = sum(A)

div = set()
for i in range(1, int(Asum ** 0.5 + 0.5) + 1):
    if Asum % i == 0:
        div.add(i)
        div.add(Asum // i)

ans = 1
for d in div:
    now = 10 ** 18
    R = [a % d for a in A]
    R.sort()
    Rsum = sum(d - r for r in R)
    Lsum = 0
    for r in R:
        Lsum += r
        Rsum -= d - r
        now = min(now, max(Lsum, Rsum))

    if now <= K:
        ans = max(ans, d)

print(ans)
