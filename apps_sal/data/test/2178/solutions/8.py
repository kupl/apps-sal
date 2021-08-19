n = int(input())
a = input().split()
d = {}
k = 0
for i in range(len(a)):
    d[a[i]] = i
for s in input().split():
    if d[s] != -1:
        c = d[s]
        print(c - k + 1, end=' ')
        for i in range(k, c + 1):
            d[a[i]] = -1
        k = c + 1
    else:
        print(0, end=' ')
