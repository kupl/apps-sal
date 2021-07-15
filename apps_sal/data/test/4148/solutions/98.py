A=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
n=int(input())
s=str(input())
t=""
for i in range(len(s)):
  for j in range(26):
    if s[i]==A[j]:
      if j+n<=25:
        t+=A[j+n]
        break
      else:
        t+=A[j+n-26]
        break

print(t)
