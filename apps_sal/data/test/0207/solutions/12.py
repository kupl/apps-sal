n = int(input())
a = list(map(int, input().split()))
if n % 2 == 1:
    if a[0] % 2 == 1 and a[n - 1] % 2 == 1:
        print('Yes')
    else:
        print('No')
else:
    print('No')
