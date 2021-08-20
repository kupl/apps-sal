a = str(input())
count = 0
for i in range(3):
    if a[i - 1] == '1':
        count += 1
print(count)
