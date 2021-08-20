(n, p) = list(map(int, input().split()))
a = list(map(int, input().split()))
sum1 = 0
pre = []
for i in range(n):
    sum1 += a[i]
    sum1 = sum1 % p
    pre.append(sum1)
post = [0 for i in range(n)]
sum1 = 0
for i in range(n - 1, -1, -1):
    post[i] = sum1
    sum1 += a[i]
    sum1 = sum1 % p
s = 0
for i in range(n):
    s = max(pre[i] + post[i], s)
print(s)
