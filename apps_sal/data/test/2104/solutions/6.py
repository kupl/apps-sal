a = list(input().split())
l = int(a[0])
r = int(a[1])
print('YES')
for i in range(l, r + 1, 2):
    print(i, i + 1)
