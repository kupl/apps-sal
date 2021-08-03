n = int(input())
l = list(input().split(' '))

flag = True
t = 0
while True:
    for i, x in enumerate(l):
        if int(x) % 2 == 0:
            l[i] = int(x) / 2
        else:
            flag = False
            break
    if flag:
        t += 1
    else:
        break

print(t)
