n = int(input())
a = input()
d = {}
count = 0
for i in range(len(a)):
    if d.get(a[i]) == None:
        d[a[i]] = 1
        count += 1
if count >= n:
    print('YES')
    d = {}
    count = 0
    i = 0
    j = 0
    while count < n - 1:
        if d.get(a[i]) == None:
            d[a[i]] = 1
            if a[j:i] != '':
                count += 1 
                print(a[j:i])
                j = i
        i += 1
    print(a[j:])            
else:
    print('NO')
