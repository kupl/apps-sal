s=input()
ans = 1000
for i in range(len(s) -2):
  ans = min(abs(int(s[i:i+3])- 753), ans)
print(ans)
