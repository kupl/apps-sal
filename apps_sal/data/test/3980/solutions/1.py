n = int(input()) + 1
print(n * n - n)
t = []
k = 1 << 20

while n:
    while k >> 1 >= n: k >>= 1
    t = [(k - 1) ^ i for i in range(k - n, n)] + t
    n = k - n

print(' '.join(map(str, t)))
