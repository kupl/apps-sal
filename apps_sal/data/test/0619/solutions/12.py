a, b, c = map(int, input().split())
print((a + b) // c, end = ' ')
if (a % c) + (b % c) >= c:
    print(min((-b) % c, (-a) % c))
else:
    print(0)
