N = int(input())
Buttons = []
for i in range(N):
    Buttons.append(int(input()))
pos = 0
count = 0
visit = [0] * N
flag = 1
while pos != 1:
    if visit[pos] != 0:
        flag = 0
        break
    else:
        visit[pos] = 1
        pos = Buttons[pos] - 1
        count = count + 1
if flag == 1:
    print(count)
else:
    print(-1)
