s = input()

def check(a):
  if len(a) % 2 == 1:
    return False
  if a[:len(a)//2] == a[len(a)//2:]:
    return True
  return False

for i in range(len(s)):
  if check(s[:-1-i]):
    print(len(s) - i - 1)
    break
