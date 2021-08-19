n = int(input())
x = input().split()
if x.count(x[0]) == n:
    print(x[n - 1])
else:
    y = []
    d = int(x[1]) - int(x[0])
    for i in range(n - 1):
        y.append(int(x[i + 1]) - int(x[i]))
    if y.count(d) == n - 1:
        print(int(x[-1]) + d)
    else:
        print(x[-1])
