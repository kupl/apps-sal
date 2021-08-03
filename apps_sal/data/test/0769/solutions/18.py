a, b, c = [int(x) for x in input().split(' ')]
a %= b
k = 0
for i in range(1, 10**4):
    a *= 10
    if (a // b) % 10 == c:
        print(i)
        k = 1
        break

if not k:
    print(-1)
