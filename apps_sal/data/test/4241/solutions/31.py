s = input()
t = input()
min = 10000
for i in range(len(s)-len(t)+1):
  count = 0
  for j in range(len(t)):
    if(s[i+j] != t[j]):
      count+=1
  if(count < min):
      min = count
print(min)
