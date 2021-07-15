N, A, B = list(map(int,input().split()))

ans = 0

for i in range(1, N+1, 1):
  stri = str(i)
  sum = 0
  for j in range(len(str(i))):
    sum += int(stri[j])
  else:
    if sum >= A and sum <= B:
      ans += i
      
print(ans)

