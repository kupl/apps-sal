from itertools import permutations as p
def f(n, tn):
    if not n:
        tn.append(0)
        return 1
    cnt = 0
    while n:
        tn.append(n % 7)
        n //= 7
        cnt += 1
    return cnt
ans = 0
tn, tm = [], []
n, m = map(int, input().split())
n -= 1
m -= 1
x, y = f(n, tn), f(m, tm)
tn, tm = tuple(tn[::-1]), tuple(tm[::-1])

s = {0, 1, 2, 3, 4, 5, 6}
if x + y > 7:
    print(0);return
for i in p(s, x):
    if i <= tn:
        for j in p(s - set(i), y):
            if j <= tm:
                ans += 1
print(ans)
