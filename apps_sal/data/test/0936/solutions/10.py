n = int(input())
a = list(map(int, input().split()))

max_n = 1
cnt = dict()
cnt[a[0]] = 1
max_ = a[0]
for i in range(1, n):
    cur_n = a[i]
    if cur_n not in cnt:
        cnt[cur_n] = 0
    cnt[cur_n] += 1
    if cnt[cur_n] > max_n:
        max_n = cnt[cur_n]
        max_ = cur_n
print(max_)

