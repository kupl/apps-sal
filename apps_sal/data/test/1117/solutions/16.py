n = int(input())
prev = 10 ** 10
for i in range(n):
    a, b = map(int, input().split())
    if max(a, b) <= prev:
        prev = max(a, b)
    elif min(a, b) <= prev:
        prev = min(a, b)
    else:
        print('NO')
        return
print('YES')
