import sys
mod = 998244353
fact = [1]
for i in range(1, 300001):
    fact.append((fact[-1] * i) % mod)


data = []
num = int(sys.stdin.readline())

l = []
for _ in range(num):
    data.append(tuple([int(i) for i in sys.stdin.readline().split()]))
    l.append(data[-1][1])

ans = 0
# f.sort()
# last = -1
# tot = 1
# run = 0
# for p in f:
#     if p == last:
#         run += 1
#     else:
#         tot = (tot * fact[run])%mod
#         run = 1
#         last = p
# tot = (tot * fact[run])%mod
# ans += tot

l.sort()
last = -1
tot = 1
run = 0
for p in l:
    if p == last:
        run += 1
    else:
        tot = (tot * fact[run]) % mod
        run = 1
        last = p
tot = (tot * fact[run]) % mod
ans += tot

data.sort()


f = [i[0] for i in data]

last = -1
tot = 1
run = 0
for p in f:
    if p == last:
        run += 1
    else:
        tot = (tot * fact[run]) % mod
        run = 1
        last = p
tot = (tot * fact[run]) % mod
ans += tot


sor = True
for i in range(num - 1):
    if data[i][1] > data[i + 1][1]:
        sor = False
        break

if sor:
    last = (-1, -1)
    tot = 1
    run = 0
    for p in data:
        if p == last:
            run += 1
        else:
            tot = (tot * fact[run]) % mod
            run = 1
            last = p
    tot = (tot * fact[run]) % mod
    # print(tot)

    ans -= tot
q = fact[num]
print((q - ans) % 998244353)
