
n = int(input())
s = [[], [], [], []]

for i in range(n):
    x = input().strip().split()
    if x[0] == "11":
        s[3].append(int(x[1]))
    elif x[0] == "10":
        s[2].append(int(x[1]))
    elif x[0] == "01":
        s[1].append(int(x[1]))
    else:
        s[0].append(int(x[1]))

ans = 0
for i in range(len(s[3])):
    ans = ans + s[3][i]
s[2] = sorted(s[2], reverse=True)
s[1] = sorted(s[1], reverse=True)
tlen = min(len(s[1]), len(s[2]))

for i in range(1, 3):
    for j in range(tlen):
        ans = ans + s[i][j]
    for j in range(tlen, len(s[i])):
        s[0].append(s[i][j])

s[0] = sorted(s[0], reverse=True)
tlen = min(len(s[3]), len(s[0]))
for i in range(tlen):
    ans = ans + s[0][i]

print(ans)
