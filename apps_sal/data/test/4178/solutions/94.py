N = int(input())
H = list(map(int,input().split()))
flg = 0
ans = "Yes"

for i in range(N-1):
  if H[i]-H[i+1] > 1:
    ans = "No"
    break
  elif H[i]-H[i+1] == 1 and flg == 0:
    flg = 1
  elif H[i]-H[i+1] == 1 and flg == 1:
    ans = "No"
    break
  elif H[i]-H[i+1] == 0:
    continue
  else:
    flg = 0
    continue

print(ans)
