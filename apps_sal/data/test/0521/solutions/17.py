n = int(input())
a = list(input()) + ['?']
f = False
for i in range(1, n):
    if a[i] == a[i - 1] and a[i] != '?':
        f = True
        break
if f:
    print('No')
    return
for i in range(n):
    if a[i] == '?':
        if a[i - 1] == a[i + 1] or a[i - 1] == '?' or a[i + 1] == '?':
            print('Yes')
            return
print('No')
