N, K = input().split()
D = list(map(int, input().split()))
ans = []
a = int(N[0])
x = 0
b = 0
while b in D:
    b += 1
c = 2
while c in D:
    c += 1
y = 0
while a == int(N[x]) and x <= len(N) - 1:
    while a in D and a <= 9:
        a += 1
    if a == 10:
        y = x
        if 0 in D:
            a += b
        if 1 in D:
            if b != 0:
                a += (b - 1) * 10
            else:
                a += (c - 1) * 10
    ans.append(str(a))
    if a != int(N[x]):
        for i in range(len(N) - 1 - x):
            ans.append(str(b))
    elif x <= len(N) - 2:
        x += 1
        a = int(N[x])
    else:
        a = int(N[x]) - 1
while y > 0:
    s = ans[y][0]
    t = ans[y][1]
    r = ans[y]
    ans[y] = t
    ans[y - 1] = str(int(ans[y - 1]) + 1)
    if int(ans[y - 1]) in D:
        u = int(ans[y - 1])
        while u in D:
            u += 1
            ans[y - 1] = str(u)
    if ans[y - 1] != "10":
        y = 0
    else:
        y -= 1
        ans[y] = r
print("".join(ans))
