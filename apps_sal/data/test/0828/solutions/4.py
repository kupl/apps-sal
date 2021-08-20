(n, root) = map(int, input().split())
a = list(map(int, input().split()))


def push(d, x, val):
    if x not in d:
        d[x] = 0
    d[x] += val
    if d[x] == 0:
        del d[x]


d = {}
for x in a:
    push(d, x, 1)
min_ = 0
root -= 1
inf = 9999999
if a[root] != 0:
    min_ += 1
    push(d, a[root], -1)
    push(d, 0, 1)
if 0 in d and d[0] > 1:
    add = d[0] - 1
    min_ += add
    push(d, inf, add)
    d[0] = 1
S = [[val, num] for (val, num) in sorted(d.items(), key=lambda x: x[0])]
cur = -1
i = 0
while i < len(S):
    remain = S[i][0] - (cur + 1)
    while remain > 0:
        (val, num) = S[-1]
        if val == S[i][0]:
            if val != inf:
                min_ += min(remain, num)
            break
        else:
            add = min(num, remain)
            remain -= add
            if val != inf:
                min_ += add
            if num == add:
                S.pop()
            else:
                S[-1][1] -= add
    cur = S[i][0]
    i += 1
print(min_)
