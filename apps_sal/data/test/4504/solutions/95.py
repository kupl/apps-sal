S=str(input())
for i in range(len(S)-1,0,-1):
    S=S[:i]
    if len(S)%2==0:
        x=len(S)//2
        if S[:x]==S[x:]:
            print(len(S))
            break
