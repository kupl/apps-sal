a, b = map(int, input().split())

difference = b - a
answer = 0
for x in range(difference):
    answer += x

print(answer - a)
