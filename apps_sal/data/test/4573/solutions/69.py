n = int(input())
x = list(map(int, input().split()))
y = sorted(x)
m = n // 2
p = y[m - 1]
q = y[m]
for i in range(n):
    if p < x[i]:
        print(p)
    else:
        print(q)
