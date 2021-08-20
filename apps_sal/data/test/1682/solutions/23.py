(n, k) = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))
dif = []
for i in range(n):
    dif.append((a[i] - b[i], i))
dif.sort()
s = 0
for i in range(k):
    s += a[dif[i][1]]
    a[dif[i][1]] = b[dif[i][1]] = 0
for i in range(len(a)):
    s += min(a[i], b[i])
print(s)
