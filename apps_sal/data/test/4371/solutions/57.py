S=input()
ans=753753753753753753753753753753
for i in range(len(S)-2):
    temp=int(S[i:i+3])
    if abs(temp-753)<ans:
        ans=abs(temp-753)
print(ans)

