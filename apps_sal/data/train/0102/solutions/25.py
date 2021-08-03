t = int(input())
for i in range(t):
    n = int(input())
    a = 9 * (len(str(n)) - 1)
    if n >= int(str(n)[0] * len(str(n))):
        print(a + int(str(n)[0]))
    else:
        print(a + int(str(n)[0]) - 1)
