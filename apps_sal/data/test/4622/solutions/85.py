def DuplicateCheck(seq):
  return len(seq) != len(set(seq))

N=input()
A=input().split()
print('NO' if DuplicateCheck(A) else 'YES')
