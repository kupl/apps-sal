q = int(input())
for i in range(q):
    c = True
    s = input()
    t = input()
    for j in s:
        if j in t:
            print('YES')
            c = False
            break
    if c:
        print('NO')
