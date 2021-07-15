n = int(input())
arr = list(map(int, input().split()))
for x in arr:
    if x < 15:
        print('NO')
        continue
    if x % 14 >= 7 or x % 14 == 0:
        print('NO')
        continue
    else:
        print('YES')


