n = int(input())
c = list(map(int,input().split()))
c.sort(reverse = True)
a = 0
b = 0
if n % 2 == 0:
    for i in range(n // 2 ):
        a += c[i * 2]
        b += c[i * 2 + 1]
else:
    for i in range(n // 2 ):
        a += c[i * 2]
        b += c[i * 2 + 1]
    a += c[n - 1]

print(a - b)
