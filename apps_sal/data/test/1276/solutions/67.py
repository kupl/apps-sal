n=int(input())
s,rem=input(),0
ans = s.count('R') * s.count('B') * s.count('G')

for i in range(1, (n-1) // 2 + 1):
  for j in range(i*2, n):
    if s[j]+s[j-i]+s[j-2*i] in ("RGB","RBG","GRB","GBR","BGR","BRG"):
      rem += 1
    
print(ans - rem)
