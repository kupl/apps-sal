n,k =[*map(int, input().split())]

ans = int(k/n)
if k %n != 0:
    ans+=1
print(ans)
