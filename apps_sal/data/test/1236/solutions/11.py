(n, k) = [int(i) for i in input().split()]
l = [int(i) for i in input().split()]
no = 0
for i in l:
    no += i % 2
ne = n - no
if n == k:
    if no % 2:
        print('Stannis')
    else:
        print('Daenerys')
elif no <= (n - k) // 2:
    print('Daenerys')
elif no % 2:
    if (n - k) % 2 and ne <= (n - k) // 2 and (ne % 2 == 0):
        print('Daenerys')
    elif (n - k) % 2 == 0 and (ne > (n - k) // 2 or ne % 2):
        print('Daenerys')
    else:
        print('Stannis')
elif (n - k) % 2 and ne <= (n - k) // 2 and ne % 2:
    print('Daenerys')
elif (n - k) % 2 == 0 and (ne > (n - k) // 2 or ne % 2 == 0):
    print('Daenerys')
else:
    print('Stannis')
