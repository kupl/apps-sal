n = int(input())
a = list(map(int, input().split()))
if n == 1:
    print(a[0])
elif n == 2:
    print(max(a[0] - a[1], a[1] - a[0]))
else:
    x = min(a)
    y = max(a)
    a = list(map(abs, a))
    print(sum(a) - (2 * min(a) if x * y > 0 else 0))
