d, n = map(int,input().split())

def cal(x):
  if x % 100 != 0: return 0
  return cal(x/100) + 1

cnt = 0
tmp = 1
while True:
  if cal(tmp) == d:
    cnt += 1
  if cnt == n:
    break
  tmp += 1
print(tmp)
