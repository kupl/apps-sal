n = int(input())
q = input().split(" ")
a = [None] * n
for i in range(0, n):
    a[i] = int(q[i])
m = int(input())
for i in range(0, m):
    q = input().split(" ")
    if int(q[0]) != n and int(q[0]) != 1:
        a[int(q[0]) - 2] = a[int(q[0]) - 2] + int(q[1]) - 1
        a[int(q[0])] = a[int(q[0])] + a[int(q[0]) - 1] - int(q[1])
        a[int(q[0]) - 1] = 0
    if int(q[0]) == n:
        if n != 1:
            a[int(q[0]) - 2] = a[int(q[0]) - 2] + int(q[1]) - 1
            a[int(q[0]) - 1] = 0
        else:
            a[int(q[0]) - 1] = 0
    if int(q[0]) == 1:
        if n != 1:
            a[int(q[0])] = a[int(q[0])] + a[int(q[0]) - 1] - int(q[1])
            a[int(q[0]) - 1] = 0
        else:
            a[int(q[0]) - 1] = 0
for i in range(0, n):
    print(a[i])
