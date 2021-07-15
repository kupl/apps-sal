S = input()
N = len(S)

def palindrome(string):
  return 0 if string==string[::-1] else 1

ls1 = S[0:int((N-1)/2)]
ls2 = S[int((N+3)/2-1):N]

#print(ls1)
#print(ls2)


if palindrome(S) == palindrome(ls1) == palindrome(ls2) == 0:
  print('Yes')
else:
  print('No')
