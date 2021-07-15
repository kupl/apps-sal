N = int(input())
A = list(map(int,input().split()))

dic = {}
for a in A:
  if a in dic:
    dic[a] += 1
  else:
    dic[a] = 1
    
dic = sorted(dic.items(), reverse=True)

ans = 1
check = 0
bool1 = False
for (i,j) in dic:
  cnt = j // 2
  for _ in range(cnt):
    ans *= i
    check += 1
    if check == 2:
      bool1 = True
      break
  if bool1:
    break

print(ans if ans != 1 else 0)
