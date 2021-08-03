n = input()
sum_index = 0
for i in n:
    sum_index += int(i)

if int(n) % sum_index == 0:
    print("Yes")
else:
    print("No")
