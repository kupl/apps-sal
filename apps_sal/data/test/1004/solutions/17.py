n = int(input())

a = list(map(int, input().split()))

days = [] #when days end
ok = True

tod = set()
now = set()



for i in range(n):
    #print(i, tod, now)
    if (a[i]>0):
        if (a[i] in tod):
            ok = False
            break
        else:
            tod.add(a[i])
            now.add(a[i])
    else:
        if not (-a[i] in now):
            ok = False
            break
        else:
            now.discard(-a[i])
    if (len(now)==0):
        days.append(i+1)
        tod = set()
        now = set()

if (len(now)!=0):
    ok = False

if (ok):
    print(len(days))
    days = [0]+days
    for i in range(1, len(days)):
        print(days[i]-days[i-1], end=' ')
else:
    print(-1)
