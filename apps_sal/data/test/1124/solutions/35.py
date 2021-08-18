def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


n = int(input())
a = list(map(int, input().split()))
ans = a[0]
for i in range(n):
    ans = gcd(ans, a[i])
print(ans)
