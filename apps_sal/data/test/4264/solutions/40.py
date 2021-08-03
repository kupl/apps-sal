a = input()
N = int(a)

if N == 10**5:
    print((90909))
elif N >= 10**4:
    print((N - (9000 + 90)))
elif N >= 10**3:
    print((909))
elif N >= 10**2:
    print((N - 90))
elif N >= 10:
    print((9))
else:
    print(N)
