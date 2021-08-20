N = int(input())
buttons = []
for _ in range(N):
    buttons.append(int(input()))
s = 1
cnt = 0
while True:
    s = buttons[s - 1]
    cnt += 1
    if s == 2:
        break
    elif cnt > N:
        cnt = -1
        break
print(cnt)
