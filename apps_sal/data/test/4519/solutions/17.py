t = int(input())
while t > 0:
    t -= 1
    n, k = list(map(int, input().split()))
    z = []
    a = list(input())
    for i in range(n):
        if a[i] == '0':
            z.append(i)
    y = 0
    for i in range(len(z)):
        if k - (z[i] - y) > 0:
            k -= (z[i] - y)
            z[i] = y
            y += 1
        else:
            z[i] -= k
            break
    v = [0 for i in range(n)]
    for i in range(len(z)):
        a[z[i]] = '0'
        v[z[i]] = 1
    for i in range(n):
        if v[i] == 0:
            a[i] = '1'
    print("".join(a))
