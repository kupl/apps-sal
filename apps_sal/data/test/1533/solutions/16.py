3
n = int(input())
w = set()
for i in range(n):
    s = input()
    if s in w:
        print('YES')
    else:
        print('NO')
    w.add(s)
