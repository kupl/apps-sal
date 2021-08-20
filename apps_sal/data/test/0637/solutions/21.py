n = int(input())
a = input().split()
s = ''.join(a)
w = set(s.split('0')) - {''}
b = set(s.split('1')) - {''}
if len(w) > 1 or len(b) > 1:
    print('NO')
elif len(w) == 0 or len(b) == 0:
    print('YES')
elif len(list(w)[0]) == len(list(b)[0]):
    print('YES')
else:
    print('NO')
