N = int(input())
blue = {}
for _ in range(N):
    s = input()
    if s in blue.keys():
        blue[s] += 1
    else:
        blue[s] = 1
M = int(input())
red = {}
for _ in range(M):
    t = input()
    if t in red.keys():
        red[t] += 1
    else:
        red[t] = 1
cnt = 0
for i in blue.keys():
    if i in red.keys():
        cnt = max(cnt, blue[i] - red[i])
    else:
        cnt = max(cnt, blue[i])
print(cnt)
