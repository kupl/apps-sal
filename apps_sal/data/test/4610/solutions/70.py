N, K = map(int, input().split())
a_list = list(map(int, input().split()))

num_dic = {}
for a in a_list:
  count = num_dic.get(a, 0)
  num_dic[a] = count + 1

replace_num = len(num_dic.keys()) - K
replace_num = 0 if replace_num < 0 else replace_num
ans = 0
for i, taple in enumerate(sorted(num_dic.items(), key = lambda x:x[1])):
  if i == replace_num:
    break
  ans += taple[1]

print(ans)
