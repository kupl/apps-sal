n = int(input())

def it():
  A = list(map(int,input().split()))
  A.reverse()

  c1 = 0
  r0 = len(A) - sum(A)
  yield r0

  for a in A:
    if a == 1:
      c1 += 1
      yield c1 + r0
    else:
      r0 -= 1

print(max(it()))



