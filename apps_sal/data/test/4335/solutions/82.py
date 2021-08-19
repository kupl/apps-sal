n = int(input())
if n % 2 == 0:
    work = int(n / 2)
    s = input()
    a = s[:work]
    b = s[work:]
    if a == b:
        print('Yes')
    else:
        print('No')
else:
    print('No')
