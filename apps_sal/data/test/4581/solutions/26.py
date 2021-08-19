a = list(input())
count = 0
for i in range(0, len(a)):
    if a[i] == 'o':
        count += 1
print(700 + count * 100)
