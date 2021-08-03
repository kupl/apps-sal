[A, B, N] = [int(i) for i in input().split()]
u = 0
s = float('inf')
if B - 1 <= N:
    t = (A * (B - 1)) // B - A * ((B - 1) // B)
else:
    u += 1
if 2 * B - 1 <= N:
    s = (A * (2 * B - 1)) // B - A * ((2 * B - 1) // B)
else:
    u += 1

print(min(s, t) if u != 2 else (A * N) // B - A * (N // B))
