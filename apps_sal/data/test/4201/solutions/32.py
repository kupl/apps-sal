h, w, k = list(map(int, input().split()))
c = [list(input()) for _ in range(h)]
ans = 0

from itertools import product
for row_bit in product(range(2), repeat=h):
  for col_bit in product(range(2), repeat=w):
    black_cnt = 0
    for i in range(h):
      for j in range(w):
        # bitに0が立っているときは塗らない
        if c[i][j] == '#' and (row_bit[i]==0 and col_bit[j]==0):
          black_cnt += 1
    if black_cnt == k:
      ans += 1
print(ans)
