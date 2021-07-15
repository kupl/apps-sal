n=int(input())
s=input()
count = 0
for i in range(n-1):
  a=s[:i + 1]
  b=s[i+1:]
  temp = 0
  for j in range(27):
    if chr(96+j) in a and chr(96+j) in b:
      temp += 1
  count = max(temp, count)
print(count)
