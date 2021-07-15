n, A = map(int, input().split())
d = list(map(int, input().split()))

s = 0
for x in d:
    s += x

for i in range(n):
    print(d[i] - (min(d[i], A - n + 1) - max(A - s + d[i], 1) + 1), end=' ')

