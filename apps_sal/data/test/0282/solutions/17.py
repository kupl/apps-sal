(n, d) = map(int, input().split())
num = 0
v = 0
a = 1
k = 0
st = input()
for i in range(1, n):
    num += 1
    if int(st[i]) == 1:
        k = num
    if num % d == 0:
        if k != 0:
            num = num - k
            v += 1
        else:
            a = 0
        k = 0
if a == 1:
    if num % d == 0:
        print(v)
    else:
        print(v + 1)
else:
    print(-1)
