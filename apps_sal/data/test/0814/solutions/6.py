
n = int(input())
a = list(map(int, input().split(" ")))

m = max(a)

w = [0] * m
r = [0] * n

for i in range(m):
    for j in range(n):
        if a[j] >= i + 1:
            w[i] += 1


for j in range(n):
    for i in range(m):
        if w[i] > n - (j + 1):
            r[j] += 1


res = [str(i) for i in r]
res = " ".join(res)
print(res)
