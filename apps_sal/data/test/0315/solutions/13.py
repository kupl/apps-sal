d = input().split()
n = int(d[0])
k = int(d[1])
d = input().split()
d = [int(x) for x in d]
S = 0
for i in range(n - 1):
    if d[i] + d[i + 1] < k:
        S += k - (d[i] + d[i + 1])
        d[i + 1] += k - (d[i] + d[i + 1])
print(S)
for i in d:
    print(i, end=' ')
