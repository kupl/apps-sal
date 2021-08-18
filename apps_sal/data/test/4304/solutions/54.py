
a, b = list(map(int, input().split()))

tmp = 1
for i in range(2, 1000):
    if i == (b - a):
        print((tmp - a))
    tmp += i
