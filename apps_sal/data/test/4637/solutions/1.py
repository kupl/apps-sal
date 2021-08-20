q = int(input())
for _ in range(q):
    (n, k) = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.sort()
    b.sort()
    b.reverse()
    i = 0
    while i < k and b[i] >= a[i]:
        a[i] = b[i]
        i += 1
    print(sum(a))
