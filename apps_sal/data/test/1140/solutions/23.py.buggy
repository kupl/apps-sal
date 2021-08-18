n = int(input())
a = list(map(int, input().split()))
equal = True
for i in range(1, n):
    if(a[i] != a[i - 1]):
        equal = False
        break
if(equal):
    print('0 %d' % (n * (n - 1) / 2))
    return

a.sort()
i, j = 1, n - 2
while(a[i] == a[i - 1]):
    i = i + 1
while(a[j] == a[j + 1]):
    j = j - 1
print('%d %d' % (a[n - 1] - a[0], i * (n - 1 - j)))
