import sys
(k, n) = [int(i) for i in sys.stdin.readline().split()]
rate = [int(i) for i in sys.stdin.readline().split()]
rem = dict()
for i in sys.stdin.readline().split():
    v = int(i)
    if v in rem:
        rem[v] += 1
    else:
        rem[v] = 1
for i in range(len(rate)):
    if i > 0:
        rate[i] += rate[i - 1]
ans = set()
ref = next(iter(rem))
for i in range(len(rate)):
    cnt = rem.copy()
    for j in range(len(rate)):
        v = ref + rate[j] - rate[i]
        if v in cnt:
            cnt[v] -= 1
            if cnt[v] == 0:
                del cnt[v]
    if len(cnt) == 0:
        ans.add(ref - rate[i])
print(len(ans))
