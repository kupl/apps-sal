n = int(input())
x = list(map(int, input().split()))
for i in range(n):
    if i == x[x[x[i] - 1] - 1] - 1:
        print('YES')
        break
else:
    print('NO')
