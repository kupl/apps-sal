n, p, q = list(map(int, input().split()))
s = input()
m = 0
while m * p <= n:
    if (n - m * p) % q == 0:
        k = m + (n - m * p) // q
        print(k)
        for i in range(m):
            print(s[p * i: p * (i + 1)])
        for i in range(k - m):
            print(s[p * m + q * i: p * m + q * (i + 1)])
        break
    m += 1
else:
    print(-1)

