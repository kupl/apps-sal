MOD = 10**9 + 7
I = lambda:list(map(int,input().split()))

n, = I()

n %= 4
if n == 1:
    print(1)
elif n == 2:
    print(1)
elif n == 3:
    print(0)
else:
    print(0)
