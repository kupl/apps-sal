from fractions import gcd
a, b = map(int, input().split())
if a == b:
    print(0)
    return
c = gcd(a, b)
div1 = dict()
div2 = dict()
a1 = a
b1 = b
c1 = c
for i in [2, 3, 5]:
    div1[i] = 0
    while a1 % i == 0:
        div1[i] += 1
        a1 //= i
    div2[i] = 0
    while b1 % i == 0:
        div2[i] += 1
        b1 //= i
ans = 0
for i in [2, 3, 5]:
    while div1[i] != div2[i]:
        if div1[i] > div2[i]:
            a //= i
            ans += 1
            div1[i] -= 1
        else:
            b //= i
            ans += 1
            div2[i] -= 1
if a != b:
    print(-1)
else:
    print(ans)
