n = int(input())
a = list(map(int, input().split()))
office = set()
ans = []
curc = 1
curday = []
for i in range(n):
    if a[i] < 0:
        if -1 * a[i] not in office:
            print('-1')
            quit()
        else:
            office.remove(-1 * a[i])
            if len(office) == 0:
                ans.append(curc)
                curc = 0
                curday = []
    elif a[i] in office:
        print(-1)
        quit()
    else:
        if a[i] in curday:
            print(-1)
            quit()
        office.add(a[i])
        curday.append(a[i])
    curc += 1
if len(office) != 0:
    print('-1')
    quit()
print(str(len(ans)))
print(' '.join((str(k) for k in ans)))
