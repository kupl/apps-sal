import sys
agGK = int(input())
for _ in range(agGK):
    n, k = map(int, input().split())
    a = [int(i) for i in input().split(' ', n - 1)]
    b = [int(i) for i in input().split(' ', n - 1)]
    a.sort()
    b.sort()
    if n - k - 1 == 0:
        g = 0
    else:
        g = n - k - 1
    for i in range(n - 1, g, -1):
        if a[n - i - 1] < b[i]:
            a[n - i - 1] = b[i]
        else:
            break
    print(sum(a))
