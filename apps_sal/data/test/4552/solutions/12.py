from itertools import product
n = int(input())
f = [list(map(int, input().split())) for _ in range(n)]
p = [list(map(int, input().split())) for _ in range(n)]
bits_l = list(product([0, 1], repeat=10))
bits_l.remove((0, 0, 0, 0, 0, 0, 0, 0, 0, 0))
ans = -float('inf')
for bits in bits_l:
    tmp_ans = 0
    for shop in range(n):
        tmp_cnt = 0
        for (i, bit) in enumerate(bits):
            if bit == 1 and f[shop][i] == 1:
                tmp_cnt += 1
        tmp_ans += p[shop][tmp_cnt]
    ans = max(ans, tmp_ans)
print(ans)
