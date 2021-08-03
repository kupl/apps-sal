n, x = input().split()
n = int(n)
X = int(x)

if X > n ** 2:
    print(0)
else:
    fin = 0
    for x in range(n):
        v = X / (x + 1)
        fin += v.is_integer() and v <= n
    print(fin)
