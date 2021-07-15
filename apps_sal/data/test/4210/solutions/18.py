from collections import Counter
c=[Counter() for i in range(11)]
n, k = map(int, input().split())
a = list(map(int, input().split()))
b = [[] for i in range(11)]

for j in range(n):

    b[len(str(a[j]))].append(a[j])
    for i in range(1, 11):
        r=(a[j] * (10 ** i))%k
        c[i][r]+=1
s = 0
for i in range(11):
    y = b[i]
    for j in range(len(y)):
        p = y[j] % k
        if p == 0:
            p = k
        p = k - p
        r = y[j] * (10 ** i) + y[j]
        if r % k == 0:
            s += c[i][p] - 1
        else:
            s += c[i][p]

print(s)
