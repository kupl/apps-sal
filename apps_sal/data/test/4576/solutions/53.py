A = int(input())
B = int(input())
C = int(input())
X = int(input())//50

ans = 0
for a, b, c in [(a, b, c) for a in range(A+1) for b in range(B+1) for c in range(C+1)]:
  if 10*a + 2*b + c == X:
    ans += 1

print(ans)
