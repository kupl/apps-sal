(N, *_LR) = map(int, open(0).read().split())
LR = list(zip(*[map(int, iter(_LR))] * 2))
ans = 0
for (l, r) in LR:
    ans += r - l + 1
print(ans)
