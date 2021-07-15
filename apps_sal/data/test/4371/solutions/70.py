s = str(input())
ans = 753
for i in range(len(s)-2):
  ch = int(s[i]+s[i+1]+s[i+2])
  if abs(ch-753) <= ans:
    ans = abs(ch-753)
print(ans)  
