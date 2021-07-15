import sys
sys.setrecursionlimit(10 ** 7)

N = int(input())
S = int(input())

if N == S:
    print(N + 1)
    return

def f(b, n):
    if n < b:
        return n
    return f(b, n // b) + n % b

ans = float('inf')

for b in range(1, int(N**0.5) + 100):
    if b > 1 and f(b, N) == S:
        ans = min(ans, b)

    q = S - b
    b = (N - q) // b
    if b > 1 and f(b, N) == S:
        ans = min(ans, b)

if ans == float('inf'):
    print(-1)
else:
    print(ans)
