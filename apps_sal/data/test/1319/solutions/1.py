MOD = 1000000007
top = 0
t = [0] * 200005
x = int(input())
y = list(map(int, input().split(' ')))

if 10**9+7 in y:
    print(0)
    quit()

base = 1

sq = True

for i in y:
    t[i] += 1
    base *= i
    base %= MOD

for i in range(200005):
    if (t[i] % 2 == 1):
        sq = False

ans = 1
powf = 1
if sq:
    for i in range(200005):
        ans *= pow(i, t[i]//2, MOD)
        ans %= MOD
        powf *= (t[i] + 1)
        powf %= (MOD - 1)
    print(pow(ans, powf, MOD))
    quit()

two = False
for i in range(200005):
    if (not two and t[i] % 2 == 1):
        two = True
        powf *= (t[i]+1)//2
    else:
        powf *= (t[i]+1)
    powf %= (MOD - 1)

print(pow(base, powf, 10**9+7))

