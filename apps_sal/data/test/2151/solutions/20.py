q = int(input())
for i in range(q):
    n = int(input())
    s = input()
    a = int(s[0])
    b = int(s[1:])
    if b <= a:
        print('NO')
    else:
        print('YES')
        print(2)
        print(a, b)
