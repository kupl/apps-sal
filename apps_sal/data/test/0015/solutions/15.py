a,b,c = input().split()
a = int(a)
b = int(b)
c = int(c)
if (a == b) or ((c > 0 and a < b or c < 0 and a > b) and a % c == b % c):
    print('YES')
else:
    print('NO')

