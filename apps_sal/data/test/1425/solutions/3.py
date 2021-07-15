n=int(input())
l=[int(i) for i in input().split()]
l.sort(reverse=1)
if l[0]<l[1]+l[2]:
    print('YES')
    ans=l[3:]
    ans=[l[1],l[0],l[2]]+ans
    print(*ans)
else:
    print('NO')
    

