n = int(input())
if n % 2 == 0:
    print(int(n * n / 2))
else:
    print(int((1 + n // 2) * n - n // 2))
ans = ''
if n % 2 == 0:
    for i in range(n):
        ans = ''
        for j in range(int(n / 2)):
            if i % 2 == 0:
                ans = ans + 'C.'
            else:
                ans = ans + '.C'
        print(ans)
else:
    for i in range(n):
        ans = ''
        for j in range(n):
            if i % 2 == 0:
                if j % 2 == 0:
                    ans = ans + 'C'
                else:
                    ans = ans + '.'
            elif j % 2 == 1:
                ans = ans + 'C'
            else:
                ans = ans + '.'
        print(ans)
