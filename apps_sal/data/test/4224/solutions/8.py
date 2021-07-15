n = int(input())
L = list(map(int,input().split()))
ans = 0

def cal(x):
  if x % 2 != 0: return 0
  return cal(x//2)+1
  
for l in L:
  ans += cal(l)

print(ans)
