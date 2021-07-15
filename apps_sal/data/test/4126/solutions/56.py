s = input()
l = len(s)

def check(a):
  n = len(a)
  if n % 2 == 0:
    for i in range(n//2):
      if a[i] != a[n-i-1]:
        return False
    return True
  else:
    for i in range((n-1)//2):
      if a[i] != a[n-i-1]:
        return False
    return True

res = "No"
if check(s):
  #print(s)
  if check(s[:(l-1)//2]):
    if check(s[(l+3)//2 - 1:]):
      res = "Yes"

print(res)
