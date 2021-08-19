# editorial参照
# 格子まで詰め込もうとしたのが困難
# 十分大きい黒白の塊一つに孤立した白黒の点を取る


a, b = list(map(int, input().split()))
k = 50
W = [["."] * (k * 2) for i in range(k)]
B = [["#"] * (k * 2) for i in range(k)]
for i in range(b - 1):
    h = (i // k) * 2
    w = (i % k) * 2
    W[h][w] = "#"


for i in range(a - 1):
    h = (i // k) * 2 + 1
    w = (i % k) * 2 + 1
    B[-h][-w] = "."

ans = [''.join(W[i]) for i in range(k)] + [''.join(B[i]) for i in range(k)]
print((100, 100))
print(('\n'.join(ans)))
