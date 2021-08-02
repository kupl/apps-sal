a = int(input())
s = set()
i = 1
while True:
    if a in s:
        print(i)
        break
    s |= {a}
    if a % 2 == 0:
        a >>= 1
    else:
        a = 3 * a + 1
    i += 1
