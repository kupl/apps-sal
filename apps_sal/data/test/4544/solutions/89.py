N = int(input())
a = list(map(int, input().split()))
a = sorted(a, reverse=True)
a_set = set(a)
a_cnt = [0] * (max(a) + 2)
for i in a:
    a_cnt[i] += 1
mcnt = 0
for j in a:
    cnt = a_cnt[j]
    if j - 1 in a_set:
        cnt += a_cnt[j - 1]
    if j + 1 in a_set:
        cnt += a_cnt[j + 1]
    mcnt = max(mcnt, cnt)
print(mcnt)
