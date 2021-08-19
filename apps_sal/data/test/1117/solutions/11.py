n = int(input())
f = 0
for i in range(n):
    if i == 0:
        (a, b) = list(map(int, input().split()))
        mini = max(a, b)
    else:
        (a, b) = list(map(int, input().split()))
        if a <= mini and b <= mini:
            mini = max(a, b)
        elif a <= mini:
            mini = a
        elif b <= mini:
            mini = b
        else:
            f = 1
if f == 1:
    print('NO')
else:
    print('YES')
