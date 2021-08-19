(N, M, H) = map(int, input().split())
FV = list(map(int, input().split()))
LV = list(map(int, input().split()))
TV = []
for n in range(N):
    row = list(map(int, input().split()))
    TV.append(row)
for r in range(N):
    for c in range(M):
        if TV[r][c] == 1:
            TV[r][c] = min(FV[c], LV[r])
for t in TV:
    for s in t:
        print(s, end=' ')
    print()
