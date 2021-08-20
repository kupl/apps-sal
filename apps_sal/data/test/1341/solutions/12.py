str1 = input()
str2 = input()
cpos = 0
for i in str2:
    if i == str1[cpos]:
        cpos += 1
print(cpos + 1)
