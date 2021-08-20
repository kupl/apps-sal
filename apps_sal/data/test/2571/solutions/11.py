n = int(input())
for i in range(n):
    length = int(input())
    l = [int(x) for x in input().split()]
    for j in range(length // 2):
        (a, b) = (l[2 * j], l[2 * j + 1])
        print(-b, a, end=' ')
    print()
