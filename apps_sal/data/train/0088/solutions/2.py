n = int(input())
a = list(map(int, input().split()))
for i in a:
    tmp = i % 14
    if i >= 15 and tmp >= 1 and (tmp <= 6):
        print('YES')
    else:
        print('NO')
