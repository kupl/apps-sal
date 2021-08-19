n = int(input())
a = [int(input()) for i in range(0, n)]
b = sorted(a)
for i in range(0, n):
    if b[-1] != a[i]:
        print(b[-1])
    else:
        print(b[-2])
