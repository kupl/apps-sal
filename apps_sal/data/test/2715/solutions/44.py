K = int(input('50\n'))
N = 50
r = (K - 1) % N + 1
a = (K - r) // N + N
print(*[a] * r + [a - r - 1] * (N - r))
