n = int(input())
user = 100001 * [-1]
for i in range(n):
    x, k = map(int, input().split())
    if user[k] == x - 1:
        user[k] = x
    elif user[k] < x - 1:
        print('NO')
        return
print('YES')
