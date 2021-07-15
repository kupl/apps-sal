x,y,z = map(int,input().split())
for ans in range(1,100000):
    if ans*y+(ans+1)*z <= x < (ans+1)*y+(ans+2)*z:
        print(ans)
        return
