N = int(input())
directions = input()
points = [int(x) for x in input().split()]
answer = -1
for i in range(0, N - 1):
    if directions[i] == 'R' and directions[i + 1] == 'L':
        if answer == -1 or answer > (points[i + 1] - points[i]) // 2:
            answer = (points[i + 1] - points[i]) // 2
print(answer)
