input()
res = 0
p = 0
for i in input().split():
    i = int(i)
    if i > 0:
        p += i
    elif p == 0:
        res += 1
    else:
        p -= 1
print(res)
