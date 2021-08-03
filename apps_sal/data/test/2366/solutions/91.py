import collections
N = int(input())
lsA = list(map(int, input().split()))
counterA = collections.Counter(lsA)
val = list(counterA.values())
lsans = []
alln = 0
for i in val:
    alln += i * (i - 1) // 2
for i in range(N):
    M = counterA[lsA[i]]
    div = M * (M - 1) // 2 - (M - 1) * (M - 2) // 2
    print(alln - div)
