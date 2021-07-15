A, B, C, D = list(map(int, input().split()))

mint = max(A, C)
maxt = min(B, D)

dt = max(0, maxt - mint)
print(dt)

