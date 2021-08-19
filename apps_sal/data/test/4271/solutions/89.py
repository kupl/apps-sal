kind = int(input())
table_1 = input().split(' ')
table_2 = input().split(' ')
table_3 = input().split(' ')
total = 0
for i in range(kind):
    total += int(table_2[i])
for j in range(kind - 1):
    if int(table_1[j]) == int(table_1[j + 1]) - 1:
        total += int(table_3[int(table_1[j]) - 1])
print(total)
