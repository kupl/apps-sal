n = int(input())
prev = 999999999999
for i in range(n):
    x = list(map(int, input().split()))
    if max(x) <= prev:
        prev = max(x)
    elif min(x) <= prev:
        prev = min(x)
    else:
        print('NO')
        return

print('YES')
