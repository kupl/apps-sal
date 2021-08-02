N = int(input())


def grundy(x, k):
    while x % k != 0:
        p = max(1, (x - x // k * k) // (x // k + 1))
        x = x - (x // k + 1) * p
    return x // k


g = 0

for _ in range(N):
    a, k = map(int, input().split())
    g ^= grundy(a, k)

print('Takahashi' if g != 0 else 'Aoki')
