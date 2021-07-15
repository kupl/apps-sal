K, N = list(map(int, input().split()))
As = list(map(int, input().split()))

As += [As[0] + K]

maxDiff = 0
for i in range(N):
    d = As[i+1]-As[i]
    if d > maxDiff:
        maxDiff = d

print((K-maxDiff))

