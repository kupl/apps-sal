from collections import defaultdict
import sys
def input(): return sys.stdin.readline().rstrip()


n = int(input())


def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a


d = defaultdict(int)
for i in range(2, n + 1):
    a = prime_factorize(i)
    for j in a:
        d[j] += 1
cnt_74 = []
cnt_2 = []
cnt_4 = []
cnt_14 = []
cnt_24 = []
for i in d:
    if d[i] >= 74:
        cnt_74.append(i)
    if d[i] >= 2:
        cnt_2.append(i)
    if d[i] >= 4:
        cnt_4.append(i)
    if d[i] >= 14:
        cnt_14.append(i)
    if d[i] >= 24:
        cnt_24.append(i)
ans = 0
ans += len(cnt_74)

for i in cnt_2:
    for j in cnt_24:
        if i != j:
            ans += 1
for i in cnt_4:
    for j in cnt_14:
        if i != j:
            ans += 1
for i in cnt_2:
    for j in range(len(cnt_4)):
        for k in range(j + 1, len(cnt_4)):
            j_ = cnt_4[j]
            k_ = cnt_4[k]
            if i != j_ and j_ != k_ and k_ != i:
                ans += 1
print(ans)
