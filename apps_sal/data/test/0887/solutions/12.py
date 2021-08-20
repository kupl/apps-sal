n = int(input())
a = list(map(int, input().split()))
if sum(a) >= 1 and sum(a) == max(1, n - 1):
    print('YES')
else:
    print('NO')
