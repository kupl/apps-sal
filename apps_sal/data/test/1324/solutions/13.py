a = [int(x) for x in input().split(' ')]
s = input()
count = 0
for i in s:
    if i == '1':
        count += a[0]
    elif i == '2':
        count += a[1]
    elif i == '3':
        count += a[2]
    else:
        count += a[3]
print(count)
