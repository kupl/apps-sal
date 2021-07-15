n = int(input())
a = list(map(int, input().split()))
d = dict()
for i in range(n):
    d[i] = 0
for e in a:
    d[e-1] += 1
for i in range(n):
    print(d[i])
