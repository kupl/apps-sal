val = input()
s_list = val.split(" ")
i_list = list(map((lambda x: int(x)), s_list))

min_take = i_list[0] / i_list[2]

if i_list[1] >= min_take:
  print("Yes")
else:
  print("No")
