(N, K) = map(int, input().split())
senbei = [0] * K
i = 0
while N > 0:
    senbei[i] += 1
    N -= 1
    if i == K - 1:
        i = 0
    else:
        i += 1
print(max(senbei) - min(senbei))
