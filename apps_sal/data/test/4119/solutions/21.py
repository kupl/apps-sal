n, m = list(map(int, input().split()))
x = list(map(int, input().split()))
x.sort()

d = []
for i in range(1, m):
    d.append(x[i] - x[i - 1])
d.sort()
d.reverse()
print((sum(d) - sum(d[:n - 1])))
