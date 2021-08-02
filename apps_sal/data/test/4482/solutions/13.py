num = int(input())
str_line = input().split(" ")
num_line = [int(n) for n in str_line]

ave = 0
for i in range(num):
    ave += num_line[i]

if ave % num == 0:
    ave //= num

else:
    if ave % num <= num / 2:
        ave //= num
    else:
        ave = -(-ave // num)

wa = 0
for i in range(num):
    temp = num_line[i] - ave
    wa += temp * temp

print(wa)
