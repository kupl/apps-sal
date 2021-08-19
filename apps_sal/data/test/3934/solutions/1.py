import sys
input = sys.stdin.readline
N = int(input())
X = [[] for i in range(N)]
for i in range(N - 1):
    (x, y) = list(map(int, input().split()))
    X[x - 1].append(y - 1)
    X[y - 1].append(x - 1)
for x in X:
    if len(x) == 2:
        print('NO')
        break
else:
    print('YES')
