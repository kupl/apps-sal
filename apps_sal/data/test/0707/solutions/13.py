import sys


def gcd(a, b):
    while a and b:
        if a >= b:
            a %= b
        else:
            b %= a
    return a | b


n, m = [int(s) for s in input().split()]
time = [int(s) for s in input().split()]
p = [int(s) for s in input().split()]
diffs = []
for i in range(len(time) - 1):
    diffs.append(time[i + 1] - time[i])
ans = max(diffs)
# print(diffs)
for i in range(len(diffs)):
    ans = gcd(ans, diffs[i])
for i in range(len(p)):
    if ans % p[i] == 0:
        print('YES')
        print(time[0], i + 1)
        return
print('NO')
