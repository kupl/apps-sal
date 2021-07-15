N = int(input())

W_list = []
check = True

for i in range(N):
  W = input()
  if i == 0:
    W_list.append(W)
    continue
    
  if W in W_list:
    check = False
    break
    
  if W_list[i-1][-1] != W[0]:
    check = False
    break
    
  W_list.append(W)
    
print(("Yes" if check else "No"))

