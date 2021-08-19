N = int(input())
g = 0
for _ in range(N):
    (x, k) = map(int, input().split())
    while x % k != 0:
        x = x - (x // k + 1) * max(1, (x - x // k * k) // (x // k + 1))
    g ^= x // k
print('Takahashi' if g != 0 else 'Aoki')
