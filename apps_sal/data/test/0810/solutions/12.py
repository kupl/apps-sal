import math
from sys import stdin

# stdin=open('input.txt','r')
I = stdin.readline

mod = 1000000007
fact = [1 for i in range(1000000 + 5)]
for i in range(2, len(fact)):
    fact[i] = fact[i - 1] * i
    fact[i] %= mod

a, b, n = list(map(int, I().split()))
c1 = chr(a + ord('0'))
c2 = chr(b + ord('0'))
# byg=(math.factorial(1000000))
ans = 0

for x in range(0, n + 1):
    now = a * x + n * b - b * x
    flag = False
    for c in str(now):
        if(c != c1 and c != c2):
            flag = True
            break

    if(not flag):
        # print(x,now)
        now = fact[n]
        y = fact[x]
        z = fact[n - x]
        asd = pow(y * z, mod - 2, mod)

        now *= asd
        now %= mod
        # now/=math.factorial(n-x)

        ans += now
        ans %= mod

print(int(ans))
