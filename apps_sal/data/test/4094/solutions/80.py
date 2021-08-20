k = int(input())
if k % 2 == 0 or k % 5 == 0:
    print(-1)
else:
    s = 1
    a = 7
    while a % k != 0:
        a = (10 * a + 7) % k
        s += 1
    print(s)
