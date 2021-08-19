def gcd(a, b):
    if a == 0:
        return b
    else:
        return gcd(b % a, a)


n = int(input())
a = input().split()
for i in range(n):
    a[i] = int(a[i])
maxi = max(a)
b = gcd(maxi - a[0], maxi - a[1])
for j in range(2, n):
    b = gcd(b, maxi - a[j])
ans = 0
for i in range(n):
    ans += (maxi - a[i]) // b
print(ans, b)
