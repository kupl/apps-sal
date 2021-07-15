n = input()
cnt = 1
for i in range(len(n)-1):
  if n[i] == n[i+1]:
    cnt += 1
  else:
    cnt = 1
  if cnt >= 3:
    print("Yes")
    return
    
print('No')
