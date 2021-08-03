import math

N = int(input())
AB = [list(map(int, input().split())) for _ in range(N)]

MOD = 1000000007

dic1 = {}
a_zero = 0
b_zero = 0
both_zero = 0

for a, b in AB:
    if a == 0 and b != 0:
        a_zero += 1
    elif a != 0 and b == 0:
        b_zero += 1
    elif a == 0 and b == 0:
        both_zero += 1
    else:
        g = math.gcd(a, b)
        a //= g
        b //= g

        if b < 0:
            a, b = -a, -b

        if (a, b) in dic1:
            dic1[(a, b)] += 1
        else:
            dic1[(a, b)] = 1

pair = []
used = set()

for key, val in list(dic1.items()):
    if key in used:
        continue

    a, b = key
    used.add((a, b))
    cnt = 0

    if a < 0:
        c, d = -b, -a
    else:
        c, d = b, a

    if (-c, d) in dic1:
        cnt += dic1.get((-c, d), 0)
        used.add((-c, d))

    pair.append((val, cnt))


all_cnt = 1
for cnt1, cnt2 in pair:
    all_cnt *= pow(2, cnt1, MOD) + pow(2, cnt2, MOD) - 1
    all_cnt %= MOD

all_cnt *= pow(2, a_zero, MOD) + pow(2, b_zero, MOD) - 1
all_cnt %= MOD

all_cnt += both_zero
all_cnt %= MOD

print(((all_cnt - 1) % MOD))
