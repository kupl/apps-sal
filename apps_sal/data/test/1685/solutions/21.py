n, q = list(map(int,input().split()))
par = n // 2 + 1
par = len(list(bin(par)[2:]))
for i in range(q):
    ui = int(input())
    si = input()
    temp = bin(ui)[2:]
    now = len(temp)
    num = list((par - now) * "0" + temp)
    now = par - now
    for i in range(len(num)):
        if str(num[i]) == '1':
            now = i
    for i in si:
        if i == "U":
            if now == 0:
                continue
            num[now] = 0
            now -= 1
            num[now] = 1
        elif i == "L":
            if str(num[-1]) == '1':
                continue
            num[now] = 0
            now += 1
            num[now] = 1
        else:
            if str(num[-1]) == '1':
                continue
            now += 1
            num[now] = 1
    for i in range(par):
        num[i] = str(num[i])
    print(int("".join(num),2))

