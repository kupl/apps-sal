n = int(input())
ai = list(map(int, input().split()))
num = sum(ai)
if n == 1:
    if num == 1:
        print('YES')
    else:
        print('NO')
elif n - num == 1:
    print('YES')
else:
    print('NO')
