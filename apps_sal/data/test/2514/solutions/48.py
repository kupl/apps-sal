n = int(input())
a = list(map(int, input().split()))
f = [0] * (int(100000.0) + 1)
sum = 0
for i in range(n):
    f[a[i]] += 1
    sum += a[i]
q = int(input())
for i in range(q):
    (b, c) = map(int, input().split())
    sum += (c - b) * f[b]
    f[c] += f[b]
    f[b] = 0
    print(sum)
