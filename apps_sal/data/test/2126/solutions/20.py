n, m, h = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
table = [list(map(int, input().split())) for i in range(n)]
answer = [[0 for i in range(m)] for j in range(n)]
for i in range(n):
    for j in range(m):
        if table[i][j] == 1:
            answer[i][j] = min(a[j], b[i])
for i in range(n):
    for j in range(m):
        print(answer[i][j], end=' ')
    print()

            

