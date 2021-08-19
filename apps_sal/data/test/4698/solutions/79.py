N = int(input())
(*T,) = map(int, input().split())
M = int(input())
px = [list(map(int, input().split())) for _ in range(M)]
for i in range(M):
    pi = px[i][0] - 1
    print(sum(T) - T[pi] + px[i][1])
