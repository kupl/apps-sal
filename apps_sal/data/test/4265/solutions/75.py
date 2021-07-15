def ans172(S:str, T:str):
    ans_count=0
    for i in range(len(S)):
        if S[i]!=T[i]:
            ans_count+=1
    return ans_count

def __starting_point():
    S=input()
    T=input()
    print(ans172(S,T))
__starting_point()
