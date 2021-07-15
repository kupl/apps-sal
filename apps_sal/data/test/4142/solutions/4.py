S = str(input())
even_list = list(S)
odd_list = []

n = 0


for i in even_list:
    add_odd = even_list.pop(n)
    odd_list.append(add_odd)
    n += 1
# 
# print(odd_list)
# print(even_list)

if "R" in even_list:
    print("No")
elif "L" in odd_list:
    print("No")
else:
    print("Yes")
