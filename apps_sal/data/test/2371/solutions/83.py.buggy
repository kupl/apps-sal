n, z, w = map(int, input().split())
a = list(map(int, input().split()))
b = [abs(a[i] - a[-1]) for i in range(n - 1)]
b = [abs(w - a[-1])] + b
if n == 1:
    print(abs(w - a[0]))
    return
print(max(abs(w - a[-1]), abs(a[-2] - a[-1])))
