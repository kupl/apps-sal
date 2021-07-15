n = int(input())
a = list(map(int, input().split()))
a.reverse()

d = [0 for i in range(n)]
d[0] = [a[0], 0]

for i in range(1, n):
    d[i] = [max(d[i-1][0], d[i-1][1] + a[i]), min(d[i-1][0], d[i-1][1] + a[i])]

print(d[-1][1], d[-1][0])
