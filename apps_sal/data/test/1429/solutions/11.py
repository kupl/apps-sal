n,s = input().split()
n = int(n)

ans = 0

for i in range(n):
  d = {"A":0,"T":0,"G":0,"C":0,}
  for j in range(i,n):
    d[s[j]] += 1
    
    if d["A"] == d["T"] and d["G"] == d["C"]:
      ans += 1
      
print(ans)
