a = input()
ans = 10000
for i in range(len(a)-2):
  ans = min(abs(753-int(a[i:i+3])),ans)
print(ans)
