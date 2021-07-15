S=input()
ans=0
for i in range(len(S)-2):
    tmp=int(S[i:i+3])
    if abs(753-tmp)<abs(753-ans):
        ans=tmp

print(abs(753-ans))
