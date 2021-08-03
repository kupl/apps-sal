N, *aa = map(int, open(0).read().split())

ans = [None] * (N // 2) + aa[N // 2:]

for i in range(N // 2, 0, -1):
    ans[i - 1] = (sum(ans[2 * i - 1::i]) % 2) ^ aa[i - 1]

p = sum(ans)
print(p)
if p:
    print(*(i + 1 for i, v in enumerate(ans) if v))
