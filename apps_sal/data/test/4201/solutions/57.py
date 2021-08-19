from itertools import product
(H, W, K) = list(map(int, input().split()))
C = []
for _ in range(H):
    c = list(input())
    C.append(c)
ans = 0
for row_bit in product(list(range(2)), repeat=H):
    for col_bit in product(list(range(2)), repeat=W):
        cnt = 0
        for row in range(H):
            for col in range(W):
                if C[row][col] == '#' and (row_bit[row] and col_bit[col]):
                    cnt += 1
        if cnt == K:
            ans += 1
print(ans)
