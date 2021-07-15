n=int(input())
P=str(input())

def ans132(n:int, P:str):
    P=list(map(int,P.split()))
    jugde_count=0
    for i in range(1,n-1):
        n_list=sorted([P[i-1],P[i],P[i+1]])
        if n_list[1]==P[i]:
            jugde_count+=1
    return jugde_count

print(ans132(n,P))
