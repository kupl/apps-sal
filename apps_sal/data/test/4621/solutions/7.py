H, W = map(int, input().split())
C = [input() for _ in range(H)]
[print(C[i // 2]) for i in range(2 * H)]
