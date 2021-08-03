def solve(n):
    p2, p3, p5 = 0, 0, 0
    while n % 2 == 0:
        n //= 2
        p2 += 1
    while n % 3 == 0:
        n //= 3
        p3 += 1
    while n % 5 == 0:
        n //= 5
        p5 += 1
    if n != 1:
        return -1
    return 2 * p3 + 3 * p5 + p2


q = int(input())
for i in range(q):
    n = int(input())
    print(solve(n))
