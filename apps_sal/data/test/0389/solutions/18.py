def scan(type):
    return list(map(type, input().split()))

a, b = scan(int)

a2 = a3 = a5 = b2 = b3 = b5 = 0

while a%2 == 0:
    a /= 2
    a2 += 1
while a%3 == 0:
    a /= 3
    a3 += 1
while a%5 == 0:
    a /= 5
    a5 += 1

while b%2 == 0:
    b /= 2
    b2 += 1
while b%3 == 0:
    b /= 3
    b3 += 1
while b%5 == 0:
    b /= 5
    b5 += 1

ans = 0
if a != b:
    print(-1)
else:
    ans += max(a2,b2) - min(a2,b2)
    ans += max(a3,b3) - min(a3,b3)
    ans += max(a5,b5) - min(a5,b5)
    print(ans)






# 1482718805944

