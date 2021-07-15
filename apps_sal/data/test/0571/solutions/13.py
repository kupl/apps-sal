n = int(input())
s = list(input())
if n % 2:
    print(':(')
    return
left = s.count('(')
right = s.count(')')
plus = 0
for i in range(n):
    if s[i] == '?':
        if left < n // 2:
            s[i] = '('
            left += 1
        else:
            s[i] = ')'
            right += 1
    if s[i] == '(':
        plus += 1
    else:
        plus -= 1
    if i != n - 1 and plus <= 0:
        print(':(')
        return
if left == n // 2 and right == n // 2:
    print(''.join(s))
else:
    print(':(')

