t = int(input())
while t:
    t -= 1
    l, r = map(int, input().split())
    if (r + 1) / 2 <= l:
        print('YES')
    else:
        print('NO')
