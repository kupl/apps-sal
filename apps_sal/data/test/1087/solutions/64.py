n, k = map(int, input().split())
arr = list(map(int, input().split()))

bit_cnt = [0] * 40

for a in arr:
    for i in range(40):
        if a >> i & 1:
            bit_cnt[i] += 1

x = 0
for i in range(39, -1, -1):
    if x + (1 << i) <= k and bit_cnt[i] <= n - bit_cnt[i]:
        x += (1 << i)

print(sum([x ^ y for y in arr]))
