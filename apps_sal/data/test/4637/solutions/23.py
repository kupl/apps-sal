t = int(input())
while t:
    n, k = map(int, input().split())
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]
    a.sort()
    b.sort(reverse=True)
    for i in range(k):
        a[i] = max(a[i], b[i])
    print(sum(a))
    t -= 1
