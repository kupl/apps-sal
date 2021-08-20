n = int(input())
a = list(map(int, input().split()))
cnt = [0] * 8
for i in a:
    cnt[i] += 1
ans = 1
if cnt[5] > 0 or cnt[7] > 0:
    ans = 0
if cnt[4] > cnt[2]:
    ans = 0
if cnt[1] != n / 3:
    ans = 0
if cnt[2] - cnt[4] + cnt[3] != cnt[6]:
    ans = 0
if ans == 0:
    print('-1\n')
else:
    while cnt[4]:
        print('1 2 4\n')
        cnt[2] = cnt[2] - 1
        cnt[4] = cnt[4] - 1
    while cnt[2]:
        print('1 2 6\n')
        cnt[2] = cnt[2] - 1
    while cnt[3]:
        print('1 3 6\n')
        cnt[3] = cnt[3] - 1
