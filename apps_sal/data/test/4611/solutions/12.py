N = int(input())
t = []
x = []
y = []
for i in range(N):
    txy = list(map(int, input().split()))
    t.append(txy[0])
    x.append(txy[1])
    y.append(txy[2])

now_x = 0
now_y = 0
now_time = 0
isOK = True
for i in range(N):
    dist = (x[i] - now_x)**2 + (y[i] - now_y)**2
    time = t[i] - now_time

    if dist <= time**2 and dist % 2 == time % 2:
        now_x = x[i]
        now_y = y[i]
        now_time = t[i]
    else:
        isOK = False
        break


if isOK:
    print("Yes")
else:
    print("No")
