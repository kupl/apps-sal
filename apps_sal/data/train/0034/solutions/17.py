n=int(input())
for i in range(n):
    d=int(input())
    if d%2==1:
        e=(d-3)//2
        s='7'+'1'*e
    else:
        e=d//2
        s='1'*e
    print(s)
