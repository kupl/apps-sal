N=int(input())
S=input()

def ans150(N:int, S:str):
    ans_count=0
    while len(S)>=3:
        if S[:3]=="ABC":
            ans_count+=1
            S=S[1:]
        else:
            S=S[1:]
    return ans_count

print(ans150(N,S))
