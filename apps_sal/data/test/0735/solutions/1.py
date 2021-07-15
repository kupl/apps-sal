n=int(input())
a=list(map(int,input().split()))
s=a.copy()
s.sort()
if a==s:
    print("yes\n1 1")
else:
    _First=-1
    _Last=-1
    for i,x in enumerate(a):
        if s[i]!=x:
            if _First==-1:
                _First=i
            _Last=i
    __First=_First
    __Last=_Last
    _b=True
    while __First<=_Last and __Last>=_First:
        if a[__First]==s[__Last]:
            pass
        else:
            _b=False
        __First+=1
        __Last-=1
    if _b:
        print("yes")
        print(str(_First+1),str(_Last+1))
    else:
        print("no")
