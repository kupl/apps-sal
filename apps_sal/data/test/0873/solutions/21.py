def turns(n, x, y):
    c = 0
    for i in range(n):
        a = abs(int(x[i]) - int(y[i]))
        if(a > 5):
            a = 10 - a
        c += a
    return c


n = int(input())
x = input()
y = input()

print(turns(n, x, y))
