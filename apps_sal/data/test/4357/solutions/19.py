n = list(map(int, input().split()))
list_num = list(n)
list_num.sort()
list_str = []
for i in list_num:
    i = str(i)
    list_str.append(i)

max_str = list_str[-1] + list_str[1]
max_int = int(max_str)
print((max_int + int(list_str[0])))
