# map(int, input().split())
rw = int(input())
for wewq in range(rw):
    n, k = list(map(int, input().split()))
    a = list(map(int, input().split()))
    a.sort()
    a.reverse()
    f = 0
    for i in range(k + 1):
        f += a[i]
    print(f)
