n = int(input())
# find A and B such that 3^A + 5^B = N
maxA = 1
maxB = 1
test = 3
while (test <= n):
    maxA = maxA + 1
    test *= 3
test = 5
while (test <= n):
    maxB = maxB + 1
    test *= 5
done = False

testA = 3
for a in range(1, maxA):
    testB = 5
    for b in range(1, maxB):
        if (testA + testB == n):
            print((str(a) + ' ' + str(b)))
            done = True
            break
        testB *= 5
    testA *= 3
if not done:
    print((-1))
