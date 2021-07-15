s = input()
l = [int(s[i:i+3]) for i in range(len(s)-2)]
ans = 753
for i in range(len(l)):
  ans = min(ans,abs(l[i]-753))
print(ans)
