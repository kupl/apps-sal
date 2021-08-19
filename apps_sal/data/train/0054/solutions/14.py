q = int(input())
for i in range(q):
    n = int(input())
    s1 = list(map(int, input().split()))
    s1.sort()
    num = 0
    for i in s1:
        if i > 2048:
            break
        num += i
    if num >= 2048:
        print('YES')
    else:
        print('NO')
