Inpt1,Inpt2=list(map(int,input().split()))
Maximum=-1
for i in range(Inpt1):
    Inpt3,Inpt4=list(map(int,input().split()))
    if Inpt4==0 and Inpt3<=Inpt2:
        Maximum=max(0,Maximum)
    elif Inpt3<Inpt2:
        Maximum=max(100-Inpt4,Maximum)
print(Maximum)

