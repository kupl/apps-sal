N = int(input())
D = [[0, 0] for i in range(N)]
for i in range(N):
    D[i] = list(map(int, input().split()))
ans = 'No'
for i in range(N - 2):
    if D[i][0] == D[i][1] and D[i + 1][0] == D[i + 1][1] and (D[i + 2][0] == D[i + 2][1]):
        ans = 'Yes'
print(ans)
