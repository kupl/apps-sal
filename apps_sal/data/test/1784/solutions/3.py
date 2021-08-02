import sys

n, k = list(map(int, input().split()))
keeps = list(map(int, input().split()))
min_k = min(keeps)
ans = [0] * n
for i in range(n):

    ans[i] = (['1'] * (min(min_k + 1, keeps[i])))
    j = 2
    while j <= k and len(ans[i]) < keeps[i]:
        ans[i].append(str(j))
        j += 1
    if len(ans[i]) < keeps[i]:
        print('NO')
        return
print('YES')
for i in range(n):
    print(' '.join(ans[i]))
