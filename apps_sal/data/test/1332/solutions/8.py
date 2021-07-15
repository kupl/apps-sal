a = list(map(int,input().split()))
ss = sum(a)
if ss%5==0 and ss>0:
    print(ss//5)
else:
    print(-1)
