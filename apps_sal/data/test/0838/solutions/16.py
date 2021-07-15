n,m = input().split()
n = int(n)
m = int(m)
cnt = 0
b = []
for i in range(n):
    a = [int(x) for x in input().split()]
    b.append(a)
    a = sum(a)
    cnt += (1<<a) + (1<<(m-a)) - 2
for i in range(m):
    x = 0
    for j in range(n):
        x = x + b[j][i]
    cnt = cnt + (1<<x) + (1<<(n-x)) - 2

cnt -= n*m
print(cnt)

