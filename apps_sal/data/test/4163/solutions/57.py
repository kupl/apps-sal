N = int(input())
D = []
ans = 'No'
for i in range(N):
    (x, y) = list(map(int, input().split()))
    if x == y:
        D.append(1)
    else:
        D.append(0)
for i in range(N - 2):
    if D[i] == D[i + 1] == D[i + 2] == 1:
        ans = 'Yes'
print(ans)
