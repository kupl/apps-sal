n=int(input())
dic={"M":0,"A":0,"R":0,"C":0,"H":0}
check=["M","A","R","C","H"]

for i in range(n):
  s=input()
  if s[0] in check:
    dic[s[0]]+=1

ans=0
for i in range(3):
  for j in range(i+1,4):
    for k in range(j+1,5):
      ans+=dic[check[i]]*dic[check[j]]*dic[check[k]]
      
print(ans)


