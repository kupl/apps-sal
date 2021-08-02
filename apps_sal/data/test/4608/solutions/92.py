n = int(input())
a = [0] * n
for i in range(n):
    a[i] = int(input())

now = 1
for i in range(1, n + 10):
    now = a[now - 1]
    if now == 2:
        print(i)
        break
else:
    print((-1))
