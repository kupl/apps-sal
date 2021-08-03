n, a, d = map(int, input().split())
it = 114945049
N = 12 * (10**9)
u = 125 * a * it % (10**9)
v = 125 * d * it % (10**9)
print(u * N + 1, v * N)
