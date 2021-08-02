N = int(input())
As = list(map(int, input().split()))

pair = [(a, i) for i, a in enumerate(As)]
pair.sort()
min_info = pair[0]
max_info = pair[-1]
# maxとminの大小関係からせめて見る
# minの絶対値が大きい->負で構成
# それ以外 -> 正で構成
print((2 * N - 1))
if abs(min_info[0]) > abs(max_info[0]):
    ind = pair[0][1]
    for i in range(N):
        print((ind + 1, i + 1))
    for i in range(N - 1, 0, -1):
        print((i + 1, i))
else:
    ind = pair[-1][1]
    for i in range(N):
        print((ind + 1, i + 1))
    for i in range(1, N):
        print((i, i + 1))
