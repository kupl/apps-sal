n = int(input())
s = list(input())
if n % 2 == 1:
    print(':(')
else:
    op = n // 2 - s.count('(')
    for i in range(n):
        if s[i] == '?':
            if op > 0:
                s[i] = '('
            else:
                s[i] = ')'
            op -= 1
    b = 0
    for i in range(n):
        if s[i] == ')':
            b -= 1
        else:
            b += 1
        if i != n - 1 and b <= 0:
            print(':(')
            break
    else:
        if b == 0:
            print(''.join(s))
        else:
            print(':(')
