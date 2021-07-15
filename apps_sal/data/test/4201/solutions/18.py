from itertools import product
h,w,k = list(map(int, input().split()))
c = [input() for i in range(h)]

ans = 0
for row_bit in product(list(range(2)), repeat= h):
    for col_bit in product(list(range(2)), repeat  = w):
        count = 0
        for row in range(h):
            for col in range(w):
                if c[row][col] == "#" and (row_bit[row] and col_bit[col]):
                    count += 1
        if count == k:
            ans += 1
print(ans)


