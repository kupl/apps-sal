a = int(input())
for i in range(a):
    ans = 0
    now = input()
    l  = len(now)
    ans = 9*(len(now)-1)
    now = int(now)
    for i in range(1,10):
        if now>=int(str(i)*l):
            ans +=1
        else:
            break
    print(ans)
