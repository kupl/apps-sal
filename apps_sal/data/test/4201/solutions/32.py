from itertools import product
h, w, k = list(map(int, input().split()))
c = [list(input()) for _ in range(h)]
ans = 0

for row_bit in product(range(2), repeat=h):
    for col_bit in product(range(2), repeat=w):
        black_cnt = 0
        for i in range(h):
            for j in range(w):
                if c[i][j] == '
                black_cnt += 1
        if black_cnt == k:
            ans += 1
print(ans)
