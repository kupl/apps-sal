def pro(g, v):
    if g == 0:
        if v == 0:
            return True
        else:
            return False
    y = 2**100
    ans = 0
    x = g
    while x != 0:
        if x >= y:
            x -= y
            ans += 1
        y //= 2
    if ans <= v and v <= g:
        return True
    else:
        return False


n, p = list(map(int, input().split()))
mini = 100000
for i in range(0, 40000):
    if n - p * i < 0:
        break
    x = pro(n - p * i, i)
    #print (x, i)
    if (x):
        #print ("YES")
        mini = min(mini, i)
if mini == 100000:
    print(-1)
else:
    print(mini)
