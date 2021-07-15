q = int(input())
for i in range(q):
    n, k = map(int, input().split())
    a = [int(i) for i in input().split()]
    if max(a) - min(a) <= 2 * k:
        print(min(a) + k)
    else:
        print(-1)
