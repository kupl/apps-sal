(N, M) = list(map(int, input().split()))
AB = [list(map(int, input().split())) for _ in range(M)]
WAY = [0] * (N + 1)
for (a, b) in AB:
    WAY[a] += 1
    WAY[b] += 1
print('\n'.join(map(str, WAY[1:])))
