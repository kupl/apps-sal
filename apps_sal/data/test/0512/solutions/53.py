n = int(input())
ab = [list(map(int, input().split())) for i in range(n)]
cnt = [0] * (2 * n)
lis = [-1] * (2 * n)
for i, (a, b) in enumerate(ab):
    if a != -1:
        if lis[a - 1] >= 0:
            print("No");return
        cnt[a - 1] = 1
        lis[a - 1] = i
    if b != -1:
        if lis[b - 1] >= 0:
            print("No");return
        cnt[b - 1] = -1
        lis[b - 1] = i
def ok(l, r):
    if min(cnt[l:(l + r) // 2]) == -1 or max(cnt[(l + r) // 2:r]) == 1:
        return False
    lis_l, lis_r = lis[l:(l + r) // 2], lis[(l + r) // 2:r]
    for i in range(len(lis_l)):
        if lis_l[i] == lis_r[i]:
            continue
        elif lis_l[i] != -1 != lis_r[i]:
            return False
        elif (lis_l[i] != -1 and lis_l[i] in lis_r) or (lis_r[i] != -1 and lis_r[i] in lis_l):
            return False
    return True
dp = [False] * (n + 1)
dp[0] = True
for i in range(n):
    if dp[i]:
        for j in range(i + 1, n + 1):
            if dp[i] == True and ok(i * 2, j * 2):
                dp[j] = True
    else:
        continue
print("Yes" if dp[-1] else "No")
