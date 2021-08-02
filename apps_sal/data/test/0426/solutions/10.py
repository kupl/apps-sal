n, s = [int(x) for x in input().split()]
a = [int(x) for x in list(input())]
counter = 0
for i in range(n):
    if counter == s:
        break
    if i == 0:
        if a[i] != 1:
            a[i] = 1
            counter += 1
    else:
        if a[i] != 0:
            a[i] = 0
            counter += 1
if len(a) == 1 and s >= 1:
    print(0)
else:
    for item in a:
        print(item, end='')
