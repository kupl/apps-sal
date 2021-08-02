n, s = int(input()), 0
a = [0] + list(map(int, input().split()))
if n % 2 == 0 or n == 1:
    print(-1)
else:
    for i in range(n, 1, -2):
        mx = max(a[i], a[i - 1])
        s += mx
        a[i // 2] = max(0, a[i // 2] - mx)
    print(s + a[1])
