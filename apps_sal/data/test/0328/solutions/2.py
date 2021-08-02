n = int(input())

answer = 0
for i in range(n):
    x, y = list(map(int, input().split()))
    answer = max(answer, x + y)

print(answer)
