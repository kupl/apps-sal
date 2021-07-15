def gcd(a, b):
    if b == 0:
        return a
    return  gcd(b, a % b)

a, b = list(map(int, input().split()))
c, d = list(map(int, input().split()))

morty = set()
cr = b
for i in range(1000):
    morty.add(cr)
    cr += a

cr = d
for i in range(1000):
    if cr in morty:
        print(cr)
        return
    cr += c
print(-1)

