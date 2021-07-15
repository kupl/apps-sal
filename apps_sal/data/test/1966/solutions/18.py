n = int(input())

answer  = []

for k in range(4):
    white_problems = 0
    black_problems = 0
    for j in range(n):
        a = [int(i) for i in list(input())]
        for x in range(n):
            if ((a[x] == 1 and x % 2 == 0) or (a[x] == 0 and x % 2 == 1)) and j % 2 == 0:
                white_problems += 1
            if ((a[x] == 1 and x % 2 == 1) or (a[x] == 0 and x % 2 == 0)) and j % 2 == 0:
                black_problems += 1
            if ((a[x] == 1 and x % 2 == 0) or (a[x] == 0 and x % 2 == 1)) and j % 2 == 1:
                black_problems += 1
            if ((a[x] == 1 and x % 2 == 1) or (a[x] == 0 and x % 2 == 0)) and j % 2 == 1:
                white_problems += 1

    answer.append([white_problems, 0])
    answer.append([black_problems, 1])
    if k != 3:
        trash = input()



answer.sort()
black = 0
white = 0
ans = 0
for i in answer:
    if black < 2 and i[1] == 1:
        ans += i[0]
        black += 1
        continue
    if white < 2 and i[1] == 0:
        white += 1
        ans += i[0]
        continue
    if white == 2 and black == 2:
        break
print(ans)

