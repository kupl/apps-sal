q = int(input())
for item in range(q):
    n, a, b = [int(x) for x in input().split()]
    counter = n // 2 * min(2 * a, b)
    if n % 2 == 1:
        counter += a
    print(counter)
