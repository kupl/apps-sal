N = int(input())
B = list(map(int,input().split()))
con = 0
for i in range(N):
  if i == 0:
    con += B[i]
  elif i == N - 1:
    con += B[N - 2]
  else:
    con += min(B[i - 1],B[i])
print(con)


