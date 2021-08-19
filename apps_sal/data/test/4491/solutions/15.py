n = int(input())
L = [list(map(int, input().split())), list(map(int, input().split()))]
ans = 0
for i in range(n):
    cnt = 0
    for j in range(n):
        if j < i:
            cnt += L[0][j]
        elif j == i:
            cnt += L[0][j] + L[1][j]
        else:
            cnt += L[1][j]
    ans = max(ans, cnt)
print(ans)
