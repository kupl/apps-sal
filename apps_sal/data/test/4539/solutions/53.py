num = input()
table = list(num)
total = 0
for i in range(len(table)):
    total += int(table[i])
if int(num) % total == 0:
    print('Yes')
else:
    print('No')
