k = int(input())

cnt = 0
step = 1
base = 1
tail = ""
now = 0
def f(x):
    s = list(str(x))
    return sum([int(i) for i in s])
while 1:
    now += step
    if now > step*f(now):
        now -= step
        step *= 10
    else:
        cnt += 1
        print(now)
        if cnt == k:
            return
     

