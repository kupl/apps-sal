import bisect

n, k = list(map(int, input().split()))
hairetu = [0] * 100001

for _ in range(n):
    a, b = list(map(int, input().split()))
    hairetu[a] += b

ruiseki = [0] * 100001
for i in range(1, 100001):
    ruiseki[i] = ruiseki[i - 1] + hairetu[i]

print((bisect.bisect_left(ruiseki, k)))
