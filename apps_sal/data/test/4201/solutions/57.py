from itertools import product

H, W, K = list(map(int, input().split()))
C = []
for _ in range(H):
    c = list(input())
    C.append(c)

# print(C)
ans = 0

for row_bit in product(list(range(2)), repeat=H):
    # print(row_bit)
    # print(row_bit[0])
    # print(row_bit[1])
    for col_bit in product(list(range(2)), repeat=W):
        # print(col_bit)
        cnt = 0
        for row in range(H):
            for col in range(W):
                if C[row][col] == "#" and (row_bit[row] and col_bit[col]):
                    cnt += 1
        if cnt == K:
            ans += 1
print(ans)
