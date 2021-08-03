n = int(input())
s = list(input())
st = s.count('X')
n2 = n // 2
k = abs(n2 - st)
if st > n2:
    for i in range(n):
        if s[i] == 'X':
            s[i] = 'x'
        if s.count('X') == n2:
            break
elif st < n2:
    for i in range(n):
        if s[i] == 'x':
            s[i] = 'X'
        if s.count('X') == n2:
            break
print(k)
print(''.join(s))
