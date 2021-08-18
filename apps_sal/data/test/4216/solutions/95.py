def divisor(n):
    l = []
    ll = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            l.append(i)
    return l


n = int(input())
l = divisor(n)
ans = 100100100100

for i in l:
    a = len(str(i))
    b = len(str(n // i))
    ans = min(ans, max(a, b))

print(ans)
