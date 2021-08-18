X, N = list(map(int, input().split()))
if N == 0:
    print(X)
    return
p = list(map(int, input().split()))

p = sorted(p)
flag = 0
x = 0
while (flag == 0):
    n = X - x
    if n in p:
        n = X + x
        if n in p:
            x += 1
        else:
            flag = 1
    else:
        flag = 1
print(n)
