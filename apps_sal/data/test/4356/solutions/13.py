N, M = list(map(int, input().split()))
A = [input() for _ in range(N)]
B = [input() for _ in range(M)]
for y in range(N - M + 1):
    for x in range(N - M + 1):
        matched = True
        for yy in range(y, y + M):
            for xx in range(x, x + M):
                if A[yy][xx] != B[yy - y][xx - x]:
                    matched = False
                if not matched:
                    break
            if not matched:
                break
        if matched:
            print('Yes')
            return
print('No')
