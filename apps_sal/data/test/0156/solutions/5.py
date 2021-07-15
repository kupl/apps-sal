def gcd(a, b):
    if(b == 0):
        return a
    else:
        return gcd(b, a % b)


n = int(input())
a, b = 1, n
for i in range(2, n):
    if i*i > n:
        break
    if n % i == 0 and gcd(i, n//i) == 1:
        a, b = i, n//i
print(a, b)

