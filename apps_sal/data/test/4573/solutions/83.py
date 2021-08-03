n = int(input())
x = list(map(int, input().split()))

y = sorted(x)
a = y[len(x) // 2]
b = y[(len(x) // 2) - 1]

for i in range(n):
    if x[i] <= b:
        print(a)
    else:
        print(b)
