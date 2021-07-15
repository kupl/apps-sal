N,K = list(map(int, input().split()))

a = [0]*K
i = 0
while N > 0:
    a[i%K] += 1
    N -= 1
    i += 1

a.sort()
print((a[K-1]-a[0]))


