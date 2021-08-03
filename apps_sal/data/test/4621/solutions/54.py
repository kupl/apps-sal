H, W = map(int, input().split())
C = [input() for _ in range(H)]

for i in range(2 * H):
    print(C[i // 2])
