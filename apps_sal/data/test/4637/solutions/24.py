t = int(input())
for i in range(t):
    n, k = map(int, input().split())
    a = [int(i) for i in input().split()]
    b = [int(i) for i in input().split()]
    s = sum(a)
    a.sort()
    b.sort()
    cnt = 0
    while cnt < len(b) and cnt < len(a) and cnt < k:
        if b[len(b) - cnt - 1] > a[cnt]:
            s += b[len(b) - cnt - 1] - a[cnt]
        cnt += 1
    print(s)
