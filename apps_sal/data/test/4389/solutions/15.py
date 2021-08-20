t = int(input())
for i in range(t):
    a = list(input())
    b = ''
    for i in range(1, len(a), 2):
        b = b + a[i]
    b = a[0] + b
    print(b)
