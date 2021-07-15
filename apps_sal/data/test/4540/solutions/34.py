input()
a = [0] + list(map(int, input().split())) + [0]
a = [j - i for i, j in zip(a, a[1:])]
x = sum(abs(i) for i in a)
for i, j in zip(a, a[1:]):
    if i * j >= 0:
        print(x)
    else:
        print(x - 2 * (min(abs(i), abs(j))))
