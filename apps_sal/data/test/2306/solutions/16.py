
N = int(input())

t = list(map(int, input().split()))
v = list(map(int, input().split()))

alltime = sum(t)
maxslis = []
rmaxslis = []


spd = 0
ans = 0

for i in range(N):

    for j in range(t[i]):
        maxslis.append(v[i])
        maxslis.append(v[i])
        rmaxslis.append(v[i])


maxslis.reverse()


for i in range(alltime * 2):

    if i == 0:
        able = 0.5
        maxslis[i] = 0

    elif able < maxslis[i]:
        maxslis[i] = able
        able += 0.5

    else:
        able = maxslis[i]

maxslis.reverse()
maxslis.append(0)

dtflag = False

for i in range(alltime * 2 + 1):

    if spd < maxslis[i]:

        ans += spd * 0.5 + 0.125
        spd += 0.5

    elif spd == maxslis[i]:

        ans += spd * 0.5
        dtflag = False

    else:
        ans += spd * 0.5 - 0.125
        spd -= 0.5
        dtflag = False

print(ans)
