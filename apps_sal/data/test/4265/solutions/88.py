a = input().split()[0]
str = input().split()[0]
count = 0
for i in range(len(a)):
    if str[i] != a[i]:
        count = count + 1
print(count)
