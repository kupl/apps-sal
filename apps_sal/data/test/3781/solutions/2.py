t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    if n%2:
        print("Second")
        continue
    d=dict()
    for num in a:
        if num not in d:
            d[num]=1
        else:
            d[num]+=1
    ok=True
    for num in d:
        if d[num]%2:
            ok=False
    if ok:
        print("Second")
    else:
        print("First")
