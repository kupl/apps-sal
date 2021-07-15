n, m, c = map(int, input().split())
b = [int(i) for i in input().split()]
a = [[int(i) for i in input().split()] for j in range(n)]

answer = 0
for i in range(n):
        x = 0
        for j in range(len(a[i])):
                x += a[i][j] * b[j]
        x += c
        if x > 0:
                answer += 1
print(answer)
