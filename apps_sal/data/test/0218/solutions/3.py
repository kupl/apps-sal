(n, p, q) = list(map(int, input().split(' ')))
s = input()
asdf = False
for i in range(n // p + 1):
    for j in range((n - i * p) // q + 1):
        if i * p + j * q == n and asdf == False:
            print(i + j)
            asdf = True
            for a in range(i):
                print(s[a * p:(a + 1) * p])
            for b in range(j):
                print(s[p * i + b * q:p * i + (b + 1) * q])
if asdf == False:
    print(-1)
