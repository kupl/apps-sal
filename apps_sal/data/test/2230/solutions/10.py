n = int(input())
vec = [x + 1 for x in range(n * n)]
m = n // 2
for i in range(n):
    for j in range(m):
        print(vec[i * m + j], end=' ')
        print(vec[-(i * m + j + 1)], end=' ')
    print()
