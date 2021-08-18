
num = int(input())
total = 0
str = input().split()
table = list(str)
for i in range(num):
    total += 1 / int(table[i])

total = 1 / total
print(total)
