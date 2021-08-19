from itertools import product

H, W, K = map(int, input().split())
c = []
ans = 0
for i in range(H):
    c.append(input())
for row_bit in product(range(2), repeat=H):
    for col_bit in product(range(2), repeat=W):
        count = 0
        # print(row_bit,col_bit)
        for row in range(H):
            for col in range(W):
                if c[row][col] == "#" and (row_bit[row] and col_bit[col]):
                    count += 1
                    # print(row,col)
        if count == K:
            ans += 1
print(ans)
