(n, k) = input().split()
n = int(n)
k = int(k)
if n < 0 or k < 0:
    pass
else:
    rem = []
    found = False
    for i in range(1, k + 1):
        check = n % i
        if check in rem:
            print('No\n')
            found = True
            break
        rem.append(check)
    if not found:
        print('Yes\n')
