N=int(input())
S=list(map(str,input()))
i=0
while i!=(len(S)-1):
    if S[i]==S[i+1]:
        S.pop(i+1)
    else:
        i+=1
print(len(S))
