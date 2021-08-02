def solve(x):
    k = 0
    while x > 0:
        if (x % 2 == 1):
            k += 1
        x //= 2
    return (2**k)


l = int(input())
ar = []
for i in range(l):
    ar.append(int(input()))
for i in range(l):
    print(solve(ar[i]))
