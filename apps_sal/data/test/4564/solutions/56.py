S=input()
for i in range(len(S)) :
  for j in range(i+1,len(S)) :
    if S[i]==S[j] :
      print("no")
      return
print("yes")
