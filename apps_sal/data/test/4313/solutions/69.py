# coding: utf-8

num = int(input())
str1 = input().split()
str2 = input().split()
str3 = []
for i in range(num):
    str3.append(int(str1[i]) - int(str2[i]))

total = 0
count = 0
for i in range(num):
    if str3[i] > 0:
        total += str3[i]
        count += 1
if count == 0:
    print((0))
else:
    print(total)

