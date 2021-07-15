S=input()
l=len(S)
ACGT=["A","G","C","T"]
count=0
ans=[]
for i in range(l):
  if S[i] in ACGT:
    count+=1
    ans.append(count)
  else:
    ans.append(count)
    count=0
print(max(ans))
