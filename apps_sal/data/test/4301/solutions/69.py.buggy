n = int(input())
a = [int(input()) for i in range(n)]
if len(set(a)) == 1:
    for i in range(n):
        print(a[0])
    return
x = sorted(a)[-1]
y = sorted(a)[-2]
for i in range(n):
    if a[i] != x:
        print(x)
    else:
        print(y)
