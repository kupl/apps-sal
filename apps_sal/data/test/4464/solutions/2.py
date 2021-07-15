A,B,C=map(int,input().split())
mod=set()
tmp=0
D=A
while tmp not in mod:
    mod.add(tmp)
    tmp=D%B
    if tmp==C:
        print('YES')
        return
    D+=A
print('NO')
