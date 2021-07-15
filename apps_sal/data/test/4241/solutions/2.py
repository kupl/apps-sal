S=input()
T=input()

def ans177(S:str, T:str):
    judge_count=0
    ans_count=0
    while judge_count<=len(S)-len(T):
        same_count = 0
        for i in range(len(T)):
            if S[judge_count+i]==T[i]:
                same_count+=1
        if same_count>=ans_count:
            ans_count=same_count
        judge_count+=1
    return len(T)-ans_count

print(ans177(S,T))
