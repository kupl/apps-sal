a = [i for i in input()]
god = False
for i in range(len(a)):
    if int(a[i]) % 2 == 0:
        god = True
        if int(a[i]) <= int(a[-1]):
            (a[i], a[-1]) = (a[-1], a[i])
            print(''.join(a))
            quit()
if not god:
    print(-1)
    quit()
if god:
    for i in range(len(a) - 1, -1, -1):
        if int(a[i]) % 2 == 0:
            (a[i], a[-1]) = (a[-1], a[i])
            print(''.join(a))
            quit()
