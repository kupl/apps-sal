num = int(input())
str1 = input()
table = list(str1)
ans = []
for i in range(num - 1):
    if table[i] == table[i + 1]:
        continue
    else:
        ans.append(table[i])
print(len(ans) + 1)
