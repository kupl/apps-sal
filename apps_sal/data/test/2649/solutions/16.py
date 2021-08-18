
N = int(input())
x_y = [list(map(int, input().split())) for _ in range(N)]


Z = []
W = []
for l in x_y:
    Z.append(l[0] + l[1])
    W.append(l[0] - l[1])

print(max((max(Z) - min(Z)), (max(W) - min(W))))
