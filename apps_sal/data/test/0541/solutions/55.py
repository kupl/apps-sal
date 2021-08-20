(N, M) = list(map(int, input().split()))
l = [list(map(int, input().split())) for _ in range(M)]
l.sort(key=lambda x: x[1])
broken_bridge = 0
position = 0
for i in range(M):
    if position < l[i][0]:
        broken_bridge += 1
        position = l[i][1] - 1
print(broken_bridge)
