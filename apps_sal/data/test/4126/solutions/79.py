s = input()
num = len(s)
n1 = s[0:(num-1) // 2]
n2 = s[(len(s)+3) // 2-1:]

if s == s[::-1] and n1 == n1[::-1] and n2 == n2[::-1]:
  print("Yes")
else:
  print("No")

