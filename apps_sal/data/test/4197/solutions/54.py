n = int(input())
an = list(map(int, input().split()))
keys = [i for i in range(1, n + 1)]

d = dict(zip(an, keys))

for i in range(1, n + 1):
    print(d[i], end=" ")
