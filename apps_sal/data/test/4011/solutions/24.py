n = int(input())
a = input()
sp = list(map(str, input().split()))
new = ''
fl1 = True
fl2 = False
for x in a:
    if int(x) > int(sp[int(x) - 1]) and (not fl1) or fl2:
        fl2 = True
        new += x
    elif int(x) < int(sp[int(x) - 1]):
        new += sp[int(x) - 1]
        fl1 = False
    else:
        new += x
print(new)
