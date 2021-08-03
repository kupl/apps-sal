def resolve():
    a = list(map(int, input().split()))
    k = int(input())
    a.sort()
    for i in range(k):
        a[2] = a[2] * 2
    print(sum(a))


resolve()
