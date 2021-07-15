n=int(input())
A=list(map(int,input().split()))
MAX = 10**18
ans = 1

for a in A:
  if a == 0:
    print(0)
    return

for a in A:
  ans *= a
  if MAX < ans:
    print(-1)
    return
print(ans)
