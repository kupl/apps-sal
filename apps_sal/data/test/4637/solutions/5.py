t = int(input())
for loop in range(t):
    (n, k) = list(map(int, input().split()))
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    for i in range(k):
        a.sort()
        b.sort()
        if a[0] < b[-1]:
            tmp = a[0]
            a[0] = b[-1]
            b[-1] = tmp
    print(sum(a))
