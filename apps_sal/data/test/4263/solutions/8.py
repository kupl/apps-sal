str1 = input()
table = list(str1)
count = 0
ans = 0
for i in range(len(str1)):
    if table[i] == 'A' or table[i] =='T' or table[i] =='C' or table[i] == 'G':
        count += 1
        if ans < count:
            ans = count
    else:
        count = 0
print(ans)
