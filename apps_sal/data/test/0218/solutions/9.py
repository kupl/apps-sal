n, p, q = list(map(int, input().split()))
s = input()

k1 = 0
k = 0

r = n // p

for i in range(r, -1, -1):
    if (n - p * i) % q == 0:
        k1 = i
        k = k1 + ((n - p * i) // q)


if k == 0:
    print(-1)
else:
    print(k)
    for i in range(k1):
        print(s[i * p: (i + 1) * p])
    for i in range(k - k1):
        print(s[p * k1 + i * q: p * k1 + (i + 1) * q])
