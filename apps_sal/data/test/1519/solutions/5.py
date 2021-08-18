

N, L, A = map(int, input().split())

total = 0
prev = 0
for _ in range(N):
    t, l = map(int, input().split())
    total += (t - prev) // A
    prev = t + l

total += (L - prev) // A

print(total)
