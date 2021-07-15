n = int(input())
data = list(map(int, input().split()))
answer = []
start = 1
finish = 1
help_set = set()
for i in range(n):
    if data[i] in help_set:
        answer.append([start, finish])
        help_set = set()
        start = finish + 1
        finish += 1
    else:
        finish += 1
        help_set.add(data[i])
if len(answer) == 0:
    print(-1)
else:
    answer[-1][-1] = n
    print(len(answer))
    for i in range(len(answer)):
        print(*answer[i])
