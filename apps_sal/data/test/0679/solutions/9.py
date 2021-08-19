a = input()
go = False
for i in range(1, len(a) - 1):
    if len(set(a[i] + a[i - 1] + a[i + 1])) == 3 and '.' not in set(a[i] + a[i - 1] + a[i + 1]):
        go = True
        break
if go:
    print('Yes')
else:
    print('No')
