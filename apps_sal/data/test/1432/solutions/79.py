n = int(input())
a = list(map(int, input().split()))
b = [0] * n
sum_r = sum(a)
tmp = 0
for i in range(n // 2 + 1):
    tmp += a[i * 2] * 2

b[0] = tmp - sum_r
for i in range(1, n):
    b[i] = a[i - 1] * 2 - b[i - 1]

print((" ".join([str(i) for i in b])))
