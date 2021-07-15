q=int(input())
for i in range(q):
    test=set()
    s=list(input())
    t=list(input())
    for item in s:
        test.add(item)
    for item in t:
        if item in test:
            print('YES')
            break
    else:
            print('NO')

