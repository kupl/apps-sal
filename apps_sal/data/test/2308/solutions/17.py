t = int(input())
for tt in range(t):
    x = input()
    y = input()
    b = list(reversed(y)).index('1')
    a = list(reversed(x))[b:].index('1')
    print(a)
