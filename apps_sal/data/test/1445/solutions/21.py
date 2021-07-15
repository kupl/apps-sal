n = int(input())
l = list(map(int, input().split()))
newl = []
if n % 2 == 0:
    rev = n // 2
else:
    rev = n // 2 + 1
flag = 1
t = n - 1
for i in range(rev):
    flag *= -1
    if flag == -1:
        newl.append(l[t])
        t -= 1
    else:
        newl.append(l[n - t - 1])
        t -= 1
t = 0
flag = -1
help = []
for i in range(rev):
    flag *= -1
    if flag == -1:
        help.append(l[n - t - 1])
    else:
        help.append(l[t])
    t += 1
if n % 2 == 0:
    newl = newl + help[::-1]
else:
    newl = newl[:-1] + help[::-1]

print(*newl)
