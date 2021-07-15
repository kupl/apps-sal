n,h,a,b,k=list(map(int,input().split()))
for i in range(k):
    ta,fa,tb,fb=list(map(int,input().split()))
    s=abs(ta-tb)
    if ((fa<a) or (fa>b)) and (ta!=tb):
        s+=min(abs(fa-a),abs(fa-b))
        if abs(fa-a)<abs(fa-b):
            e=a
        else:
            e=b
        s+=abs(fb-e)
    else:
        s+=abs(fa-fb)
    print(s)

