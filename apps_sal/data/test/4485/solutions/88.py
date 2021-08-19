(n, m) = list(map(int, input().split()))
a = [0] * m
b = [0] * m
for i in range(m):
    (a[i], b[i]) = list(map(int, input().split()))
'\ncheck = 0\n\n\nfor i in range(m):\n    if a[i] == 1:\n        check = b[i]\n        for j in range(m):\n            if a[j] == check and b[j] == n:\n                print("POSSIBLE")\n                return\n\nprint("IMPOSSIBLE")\n\n'
start = []
leave = []
for i in range(m):
    if a[i] == 1:
        start.append(b[i])
    elif b[i] == n:
        leave.append(a[i])
if set(start) & set(leave):
    print('POSSIBLE')
else:
    print('IMPOSSIBLE')
