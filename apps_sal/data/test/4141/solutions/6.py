N = int(input())
A = list(map(int, input().split()))
judge = 'APPROVED'
for Ai in A:
  if Ai % 2 == 0:
    if Ai % 6 != 0 and Ai % 10 != 0:
      judge = 'DENIED'
      break
print(judge)
