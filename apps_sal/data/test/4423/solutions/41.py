N = int(input())
r_list = []
for i in range(N):
  item = input().split()
  item[1] = int(item[1])
  item.insert(0, i + 1)
  r_list.append(item)

r_list.sort(key = lambda x: x[2], reverse = True)
r_list.sort(key = lambda x: x[1])
for item in r_list:
  print(item[0])
