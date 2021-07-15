x,y =map(int,input().split())
ans = 1
for i in range(10**7):
    if x * 2 > y:
        print(ans)
        break
    else:
        x *= 2
        ans += 1
