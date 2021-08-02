def f(a):
    k = 0
    s = len(str(a))
    for i in range(1, s):
        k += (int("9" * i) - int("1" + "0" * (i - 1)) + 1) * i
    k += (a - int("1" + "0" * (s - 1)) + 1) * s
    return(k)


a = int(input())
print(f(a))
