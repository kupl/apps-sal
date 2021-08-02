p, y = [int(x) for x in input().split()]
res = -1
for i in range(y, p, -1):
    flag = True
    for a in range(2, min(p + 1, int(i**0.5) + 1)):
        if i % a == 0:
            flag = False
            break
    if flag:
        res = i
        break
print(res)
