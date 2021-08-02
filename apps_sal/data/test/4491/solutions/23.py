n = int(input())

a = [[int(i) for i in input().split()] for j in range(2)]

sentou = []
usiro = []

for i in range(n):
    if i == 0:
        sentou.append(a[0][0])
        usiro.append(a[1][-1])
    else:
        sentou.append(a[0][i] + sentou[-1])
        usiro.append(a[1][-i - 1] + usiro[-1])

usiro = usiro[::-1]
ans = []
for i in range(n):
    ans.append(sentou[i] + usiro[i])
print(max(ans))
