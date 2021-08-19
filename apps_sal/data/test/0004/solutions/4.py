def lucky(a, b):
    return '7' in str(a) + str(b)


x = int(input())
t = 0
(h, m) = list(map(int, input().split()))
while not lucky(h, m):
    t += 1
    m -= x
    while m < 0:
        m += 60
        h -= 1
    h %= 24
print(t)
