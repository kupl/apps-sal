
N, M = list(map(int, input().split()))
A = [[] for _ in range(8)]

for i in range(N):
    x, y, z = list(map(int, input().split()))
    A[0].append(x + y + z)
    A[1].append(x + y - z)
    A[2].append(x - y + z)
    A[3].append(x - y - z)
    A[4].append(-x + y + z)
    A[5].append(-x + y - z)
    A[6].append(-x - y + z)
    A[7].append(-x - y - z)

ans = 0
for i in range(8):
    A[i].sort(reverse=True)
    ans = max(ans, sum(A[i][0:M]))
print(ans)
