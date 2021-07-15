n = int(input())
a = list(map(int, input().split()))

c = 0

for i in range(1, n-1):
    if a[i] > a[i-1] and a[i] > a[i+1]:
        c +=1
    if a[i] == a[i-1] or a[i] == a[i+1]:
        print('NO')
        return
    if a[i] <= a[i-1] and a[i] <= a[i+1]:
        print('NO')
        return
if c>1:
    print('NO')
else:
    print('YES')
