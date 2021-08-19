N = int(input())
A = list(map(int, input().split()))
cnt = [0] * 3
for x in A:
    x %= 4
    if x == 0:
        cnt[2] += 1
    elif x == 2:
        cnt[1] += 1
    else:
        cnt[0] += 1
if cnt[0] <= cnt[2] or (cnt[1] == 0 and cnt[0] == cnt[2] + 1):
    print('Yes')
else:
    print('No')
