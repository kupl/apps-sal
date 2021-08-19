from itertools import product
(h, w, k) = list(map(int, input().split()))
table = [list(input()) for _ in range(h)]
ans = 0
for row_bit in product(list(range(2)), repeat=h):
    for col_bit in product(list(range(2)), repeat=w):
        tmp = 0
        for row in range(h):
            for col in range(w):
                if table[row][col] == '#' and (row_bit[row] and col_bit[col]):
                    tmp += 1
        if tmp == k:
            ans += 1
print(ans)
