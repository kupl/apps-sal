T = int(input())

for t in range(T):
    a = input()
    b = a[0]
    for i in range(1, len(a) - 1, 2):
        b += a[i]
    b += a[-1]
    print(b)
