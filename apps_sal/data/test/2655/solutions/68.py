n = int(input())
p_list = input().split()
p_list = map(int,p_list)
p_list = sorted(p_list,reverse=True)
ans_list = []
ans = 0
for i in range(0,len(p_list)):
  if i!=0:
    ans_list.append(p_list[i])
    ans_list.append(p_list[i])
  else:
    ans_list.append(p_list[i])
for i in range(0,n-1):
	ans += int(ans_list[i])
print(ans)
