input()
a = list(map(int,input().split()))
s = sorted(a)
while a:
    for i in range(1,len(a)):
        if a[i] > a[i - 1] + 1 or a[i] + 1 < a[i - 1]:
            print('NO')
            return
    a.remove(max(a))
print('YES')
