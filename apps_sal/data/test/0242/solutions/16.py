a = int(input())
s = 0
i = 0
while s < a:
    i += 5
    t = i
    while t % 5 == 0:
        s += 1
        t /= 5

if s == a:
    print(5)
    for j in range(0, 5):
        print(i + j, end=' ')
else:
    print(0)
