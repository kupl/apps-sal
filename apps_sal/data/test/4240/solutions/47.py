S=input()
T=input()

def ans103(S:str, T:str):
    jugde_count=0
    for i in range(0,len(S)):
        S=S[-1]+S[:-1]
        if T==S:
            jugde_count+=1
    if jugde_count>0:
        return "Yes"
    else:
        return "No"

print(ans103(S,T))
