import sys
k = int(input())

a = 7
a = a % k
for i in range(1000000):
    if a == 0:
        print((i + 1))
        return
    else:
        a = 10 * a + 7
        a = a % k

print("-1")
