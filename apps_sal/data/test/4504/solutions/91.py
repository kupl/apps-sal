s = input()
n = len(s)
for i in range(2,n,2):
  if s[0:(n-i)//2] == s[(n-i)//2:n-i]:
    print(len(s[0:n-i]))
    break
