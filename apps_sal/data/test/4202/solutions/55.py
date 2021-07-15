L, R = map(int, input().split(' '))
rst = float('inf')
if R > L + 2019 * 2:
    R = R % 2019 + 2019
else:
    R %= 2019
L %= 2019
for i in range(L, R + 1):
    for j in range(i + 1, R + 1):
        rst = min(rst, (i * j) % 2019)
print(rst)
