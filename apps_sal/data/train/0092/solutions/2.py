q = int(input())
for z in range(q):
    s = input()
    t = input()
    for c in s:
        if c in t:
            print('YES')
            break
    else:
        print('NO')
