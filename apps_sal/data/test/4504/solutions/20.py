s = input()

def judge(S):
   if (len(S) % 2 == 0) and (S[:len(S) // 2] == S[(-1) * len(S) // 2:]):
      return True
   else:
      return False

for i in range(len(s)):
   s = s[:-1]
   if judge(s):
      print(len(s))
      break
