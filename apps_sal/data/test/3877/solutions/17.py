n, l, r = list(map(int, input().split()))
ln = 0
ans = 0
curr = 1
while curr <= n:
    curr *= 2
    ln += 1
ln -= 1
for i in range(l, r + 1):
    if curr > i:
        res = 1
        res2 = 0
        while (res & i) == 0:
            res *= 2
            res2 += 1
        if res2 <= ln:
            msk = n & (1 << (ln - res2))
            ans += (msk != 0)
print(ans)
