n, m, h = map(int, input().split())
top = list(map(int, input().split()))
left = list(map(int, input().split()))

matrix = [list(map(int, input().split())) for i in range(n)]
for i in range(n):
    for j in range(m):
        if matrix[i][j] == 1:
            print(min(left[i], top[j]), end=" ")
        else:
            print(0, end=" ")
    print()
