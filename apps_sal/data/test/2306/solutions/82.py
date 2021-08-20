N = int(input())
tlist = list(map(int, input().split()))
vlist = list(map(int, input().split()))
vlist.append(0)
flag = True
while flag:
    flag = False
    for i in range(N):
        if vlist[i] - vlist[i + 1] > tlist[i]:
            vlist[i] = vlist[i + 1] + tlist[i]
            flag = True
speed = 0
x = 0
for i in range(N):
    ti = tlist[i]
    vi = vlist[i]
    vj = vlist[i + 1]
    if vi <= vj:
        if vi - speed <= ti:
            x += ti * vi - (vi - speed) ** 2 / 2
            speed = vi
        else:
            x += ti * (speed + ti) - ti ** 2 / 2
            speed += ti
    elif speed + ti <= vj:
        x += ti * (speed + ti) - ti ** 2 / 2
        speed += ti
    elif 2 * vi - speed - vj <= ti:
        x += ti * vi - (vi - speed) ** 2 / 2 - (vi - vj) ** 2 / 2
        speed = vj
    else:
        a = (ti + vj - speed) / 2
        x += a * (2 * speed + a) / 2 + (ti - a) * (2 * vj + ti - a) / 2
        speed = vj
print(x)
