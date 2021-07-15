a = input()[::-1]
count = 0
for i in range(len(a)):
    if a[i] == '7':
        count += 2 ** i * 2
    else:
        count += 2 ** i
print(count)
