t = int(input())
s = ''
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    Min = 1000000001
    ans = a[0]

    for x, y in zip(a[:-k], a[k:]):
        if y - x < Min:
            ans = (x + y) // 2
            Min = y - x
    s += str(ans) + '\n'
print(s)
