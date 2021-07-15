n = int(input())
cl = list(map(int, input().split()))
if n<2:
    print(-1)
elif n==2:
    if cl[0]!=cl[1]:
        print('1')
        print('1')
    else:
        print(-1)
else:
    print(1)
    print(cl.index(min(cl))+1)
