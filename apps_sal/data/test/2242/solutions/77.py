S = list(map(int, list(input())))

pops = 0
digi = 1
cnt = [0] * 2019
cnt[0] = 1

while S:
    s = S.pop()

    pops = (pops + s * digi) % 2019
    digi = (10 * digi) % 2019

    cnt[pops] += 1

ans = 0

for i in range(2019):
    ans += cnt[i] * (cnt[i] - 1) // 2

print(ans)
