a, b = map(int, input().split())
t = a
count = 1
if b != 1:
    while t < b:
        t += (a - 1)
        count += 1
    print(count)
else:
    print(0)
