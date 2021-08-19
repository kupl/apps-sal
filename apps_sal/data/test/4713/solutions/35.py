# coding: utf-8

num = input()
count = 0
max = 0
message = input()
table = list(message)
for i in table:
    if i == "I":
        count += 1
    elif i == "D":
        count -= 1
    if max <= count:
        max = count
print(max)
