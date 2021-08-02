import collections
N = int(input())
lsA = list(map(int, input().split()))
counterA = collections.Counter(lsA)
ans = 0
for X in range(1, 10**5 + 1):
    b1 = counterA[X - 1]
    b2 = counterA[X]
    b3 = counterA[X + 1]
    ans = max(ans, sum([b1, b2, b3]))
print(ans)
