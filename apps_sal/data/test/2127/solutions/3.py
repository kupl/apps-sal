x, y = 0, 0
res = ''
n = int(input())
for _ in range(n):
    q = [i for i in input().split()]
    q[1] = int(q[1])
    q[2] = int(q[2])
    if q[0] == '+':
        x = max(x, min(q[1], q[2]))
        y = max(y, max(q[1], q[2]))
    elif x <= min(q[1], q[2]) and y <= max(q[1], q[2]):
        res += 'YES\n'
    else:
        res += 'NO\n'
print(res)
