S=input()
cnt=0
for i in range(len(S)):
    if i%2==int(S[i]):
        cnt+=1
print((min(cnt,len(S)-cnt)))

