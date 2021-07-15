n = int(input())
a = int(input())

div = n % 500
if div <= a:
    print('Yes')
else:
    print('No')
