
num = int(input())
str = input().split()
table = list(str)
table5 = [int(i) for i in table]
count = 0
table2 = sorted(table5)
table3 = [int(i) for i in table2]
for i in range(num):
    if table5[i] == table3[i]:
        continue
    else:
        count += 1

if count == 2 or count == 0:
    print("YES")
else:
    print("NO")
