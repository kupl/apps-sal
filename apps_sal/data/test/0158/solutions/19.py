n = int(input())
data = list(map(int, input().split()))
data.sort()
if n == 1 and data[0] == data[1] or data[0] == data[-1] or data[n] == data[n - 1]:
    print('NO')
else:
    print('YES')
