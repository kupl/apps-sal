def mi():
    return map(int, input().split())


for _ in range(int(input())):
    a = list(input())
    b = list(input())
    c = list(input())
    np = False
    for i in range(len(a)):
        if a[i] == c[i] or b[i] == c[i]:
            continue
        np = True
        break
    if np:
        print('NO')
    else:
        print('YES')
