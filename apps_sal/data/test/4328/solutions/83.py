
str_line = input().split(" ")
num_1 = int(str_line[0])
num_2 = int(str_line[1])

if num_2%num_1 == 0:
    ans = num_1 + num_2
else:
    ans = num_2 - num_1

print(ans)
