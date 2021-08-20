from collections import Counter
import sys
input = sys.stdin.readline
MOD = 998244353
INF = 10 ** 10
n = int(input())
s = []
a_s = []
b_s = []
for i in range(n):
    (a, b) = [int(item) for item in input().split()]
    s.append((a, b))
    a_s.append(a)
    b_s.append(b)
s.sort()
s.append((INF, INF))
facs = [1] * (n + 1)
ans = 1
for i in range(1, n + 1):
    facs[i] = facs[i - 1] * i % MOD
ans = facs[n]
pa = 0
pb = 0
both_cnt = 1
same = 1
for (a, b) in s:
    if a == pa and b == pb:
        same += 1
    else:
        if b < pb:
            both_cnt = 0
            break
        both_cnt *= facs[same]
        both_cnt %= MOD
        same = 1
    pa = a
    pb = b
acnt = Counter(a_s)
first_cnt = 1
for key in acnt.keys():
    first_cnt *= facs[acnt[key]]
    first_cnt %= MOD
bcnt = Counter(b_s)
second_cnt = 1
for key in bcnt.keys():
    second_cnt *= facs[bcnt[key]]
    second_cnt %= MOD
print((ans - (first_cnt + second_cnt - both_cnt) + MOD) % MOD)
