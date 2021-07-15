#[int(i) for i in input().split()]
a = input()
b = input()
a = a + b[::-1]
a = a.replace('X', '')
i = a.find('A')
a = a[i:] + a[:i]

c = input()
d = input()
c = c + d[::-1]
c = c.replace('X', '')
i = c.find('A')
c = c[i:] + c[:i]
if a == c:
    print('YES')
else:
    print('NO')

