n = int(input())
a = [0] * 4
i = 0
for i in range(4):
    a[i] = n % 2
    n = n // 2
a[3] = a[3] ^ 1
a[2] = a[3] ^ a[2]
a[1] = (a[3] and a[2]) ^ a[1]
a[0] = (a[3] and a[2] and a[1]) ^ a[0]
sum_ = 0
for i in range(4):
    sum_ += a[i] * 2 ** i
print(sum_)
