n = int(input())
arr = list(map(int, input().split()))
d = {}
for (i, a) in enumerate(arr, 1):
    d[i] = a
d = sorted(d.items(), key=lambda x: x[1])
for x in dict(d).keys():
    print(x, end=' ')
