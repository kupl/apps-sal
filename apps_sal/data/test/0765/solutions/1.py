T, S, q = list(map(int, input().split()))
zap = 0
while S < T:
    S = S * q
    zap += 1
print(zap)
