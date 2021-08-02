n = int(input())
a = list(map(int, input().split(' ')))
s = sum(a)
if s >= n * 4.5:
    print(0)
else:
    x = n * 4.5 - s
    i = 0
    a.sort()
    while x > 0:
        x -= 5 - a[i]
        i += 1
    print(i)
