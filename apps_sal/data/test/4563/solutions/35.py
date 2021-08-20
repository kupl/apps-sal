N = int(input())
ballots = [list(map(int, input().split())) for _ in range(N)]


def eceil(x, y):
    return (x + y - 1) // y


prev = ballots[0]
for i in range(1, N):
    (m, n) = ballots[i]
    k = max(eceil(prev[0], m), eceil(prev[1], n))
    tot = k * (m + n)
    prev[0] = tot * m // (m + n)
    prev[1] = tot * n // (m + n)
print(sum(prev))
