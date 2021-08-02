n = int(input())
ans = True
prev = 1 << 100
for i in range(n):
    a, b = sorted(list(map(int, input().split())))
    if b <= prev:
        prev = b
    elif a <= prev:
        prev = a
    else:
        ans = False
        break
print('YES' if ans else 'NO')
