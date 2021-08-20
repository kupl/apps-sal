n = int(input())
s = input()
result = True
if n == 1 and s == '0':
    result = False
if '11' in s or '000' in s:
    result = False
if s[0:2] == '00' or s[n - 2:n] == '00':
    result = False
if result:
    print('Yes')
else:
    print('No')
