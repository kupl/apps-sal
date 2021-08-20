n = int(input())
k = [input(), input()]
rt = 1
i = 0
pre = 0
mods = 1000000007
while i < n:
    if i > 0:
        if k[0][i] == k[1][i]:
            if pre:
                rt *= 2
            pre = 1
            i += 1
        else:
            if pre:
                rt *= 2
            else:
                rt *= 3
            pre = 0
            i += 2
    elif k[0][i] == k[1][i]:
        rt *= 3
        pre = 1
        i += 1
    else:
        rt *= 6
        pre = 0
        i += 2
    rt %= mods
print(rt)
