import sys
input = sys.stdin.readline
N = int(input())
dist = [list(map(int, input().split())) for i in range(N)]
ans = sum([sum(dist[i]) for i in range(N)])
for i in range(N):
    dist[i][i] = float('inf')
ans //= 2


def main(ans):
    for i in range(N):
        for j in range(i + 1, N):
            Min = min(map(sum, zip(dist[i], dist[j])))
            if Min < dist[i][j]:
                return -1
            if Min == dist[i][j]:
                ans -= dist[i][j]
    return ans


print(main(ans))
