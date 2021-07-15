N = int(input())
T = input()
S = "110"*(10**5)
ans = 0

for n in range(3):
  if S[n:n+N]==T:
    ans+=10**10-(N+n-1)//3

print(ans)
