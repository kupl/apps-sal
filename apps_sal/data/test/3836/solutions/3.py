n = int(input())
su0 = []
su1 = []
su00 = []
su11 = []
ans = 0
for i in range(n):
    (sup, val) = map(int, input().split())
    if sup == 0:
        su00.append(val)
    elif sup == 11:
        su11.append(val)
    elif sup == 1:
        su0.append(val)
    else:
        su1.append(val)
su0.sort()
su1.sort()
su11.sort()
su00.sort()
while len(su1) != 0 and len(su0) != 0:
    ans += su1[len(su1) - 1] + su0[len(su0) - 1]
    su1.pop()
    su0.pop()
while len(su11) != 0 and len(su00) != 0:
    if len(su1) != 0:
        k = 1
    elif len(su0) != 0:
        k = 0
    else:
        k = 2
    if k == 0:
        if su00[len(su00) - 1] > su0[len(su0) - 1]:
            ans += su11[len(su11) - 1] + su00[len(su00) - 1]
            su11.pop()
            su00.pop()
        else:
            ans += su11[len(su11) - 1] + su0[len(su0) - 1]
            su11.pop()
            su0.pop()
    elif k == 1:
        if su00[len(su00) - 1] > su1[len(su1) - 1]:
            ans += su11[len(su11) - 1] + su00[len(su00) - 1]
            su11.pop()
            su00.pop()
        else:
            ans += su11[len(su11) - 1] + su1[len(su1) - 1]
            su11.pop()
            su1.pop()
    else:
        ans += su11[len(su11) - 1] + su00[len(su00) - 1]
        su11.pop()
        su00.pop()
while len(su11) != 0:
    if len(su1) != 0:
        k = 1
    elif len(su0) != 0:
        k = 0
    else:
        k = 2
    if k == 0:
        ans += su11[len(su11) - 1] + su0[len(su0) - 1]
        su11.pop()
        su0.pop()
    elif k == 1:
        ans += su11[len(su11) - 1] + su1[len(su1) - 1]
        su11.pop()
        su1.pop()
    else:
        ans += su11[len(su11) - 1]
        su11.pop()
print(ans)
