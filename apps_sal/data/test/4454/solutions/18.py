q = int(input())
for _ in range(q):
    n = int(input())
    a = [int(x) for x in input().split()]
    print((sum(a) + n - 1) // n)
