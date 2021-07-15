num = int(input())
table = list(map(int, input().split()))
table2 = []
for i in range(num):
    table2.append(0)

for j in range(len(table)):
    table2[table[j]-1] += 1

for k in table2:
    print(k)

