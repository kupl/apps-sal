n = int(input())
maxA = 1
maxB = 1
while (3**maxA <= n):
    maxA = maxA + 1
while (5**maxB <= n):
    maxB = maxB + 1
done = False
for a in range(1, maxA):
    for b in range(1, maxB):
        if (3**a + 5**b == n):
            print((str(a) + ' ' + str(b)))
            done = True
            break
if not done:
    print((-1))
