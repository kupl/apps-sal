(n, k) = map(int, input().split())
s = list(input())
ans = 0
tran = 0
for i in range(n - 1):
    chk = s[i] + s[i + 1]
    if chk == 'LR' or chk == 'RL':
        tran += 1
    else:
        ans += 1
if k * 2 >= tran:
    print(n - 1)
else:
    print(ans + k * 2)
