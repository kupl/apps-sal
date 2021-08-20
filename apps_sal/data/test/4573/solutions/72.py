n = int(input())
x = list(map(int, input().split()))
x2 = sorted(x)
a = x2[n // 2 - 1]
b = x2[n // 2]
for i in range(n):
    if x[i] <= a:
        print(b)
    else:
        print(a)
