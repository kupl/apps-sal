n = int(input())
a = list(map(int, input().split()))
b = []

def gcd(x, y) :
    while y :
        x, y = y, x % y
    return x + y

for i in range(0, n) :
    b.append(a[i])
    if i + 1 < n and gcd(a[i], a[i + 1]) != 1 : b.append(1)

print(len(b) - n)
for x in b : print(x, end = ' ')

