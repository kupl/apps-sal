N, K = map(int, input().split())
A = list(map(int, input().split()))
S = sum(A)


def isOk(n):
    B = [a % n for a in A]
    B.sort()

    now = 0
    S = sum(B)
    for i, b in enumerate(B[: -1]):
        now += b
        S -= b
        if now == n * (N - i - 1) - S and now <= K:
            return True
    return False


ans = 1
for i in range(1, int(S**0.5) + 100):
    if S % i != 0:
        continue
    j = S // i

    if isOk(i):
        ans = max(ans, i)
    if isOk(j):
        ans = max(ans, j)

print(ans)
