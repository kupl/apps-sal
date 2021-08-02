q = int(input())

for i in range(q):
    n, k = tuple([int(x) for x in input().split()])
    a = [int(x) for x in input().split()]
    if (max(a) - min(a) > 2 * k):
        print(-1)
    else:
        print(min(a) + k)
