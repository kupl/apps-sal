N = int(input())
A = [int(x) for x in input().split()]
from collections import defaultdict as dd
Sieve = dd(lambda:0)
for a in A:
    Sieve[a] += 1

ans, extra = 0, 0 #extra:同じ数を3枚選んで食べるという操作で「被りカードなし」にできない種類数
for v in list(Sieve.values()):
    ans += 1
    if v > 1 and (v-1)&1:
        extra += 1
#extraから2枚選んで食べれば全体の種類数を減らさずに済む
print((ans if not extra&1 else ans-1))

