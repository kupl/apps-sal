def chunks(l, n):
  for i in range(0, len(l), n):
    yield l[i:i+n]

def palindrome(s):
  for i in range(len(s)):
    if s[i] != s[-(i+1)]:
      return False
  else:
    return True

import sys
data, num = sys.stdin.readlines()
data = data.strip()
num = int(num.strip())


if num > len(data):
  print("NO")
elif num == len(data):
  print("YES")
else:
  if len(data) % num == 0:
    for c in chunks(data, int(len(data)/num)):
      if not palindrome(c):
        print("NO")
        return
    else:
      print("YES")
  else:
    print("NO")

