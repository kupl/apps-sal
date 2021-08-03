a = list(map(int, input().split()))
if(a[0] > 1) & (a[1] == 1):
    print(-1)
elif a[0] == a[1] == 1:
    print('a')
elif a[1] > a[0]:
    print(-1)
else:
    print('ab' * ((a[0] + 2 - a[1]) // 2) + 'a' * ((a[0] - a[1]) % 2) + ''.join([chr(ord('c') + x) for x in range(a[1] - 2)]))
