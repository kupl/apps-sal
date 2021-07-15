S=input()
left=0
while S[left]!='A':
    left+=1
right=len(S)-1
while S[right]!='Z':
    right-=1
print((right-left+1))

