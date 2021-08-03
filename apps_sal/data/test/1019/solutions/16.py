def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


n = int(input())
for i in range(1, n):
    if i > n - i and gcd(i, n - i) == 1:
        print(n - i, i)
        break
