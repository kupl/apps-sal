a = list(str(input()))
b = list(str(input()))
count = 0
for i in range(len(a)):
    if a[i] != b[i]:
        count += 1
print(count)
