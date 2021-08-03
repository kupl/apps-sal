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
    R = [a % d for a in A]
    R.sort()
    r = sum(R) // d
    l = N - r
    need = sum(R[:l])
    if need <= K:
        ans = max(ans, d)
print(ans)
