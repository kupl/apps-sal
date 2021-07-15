t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    d = [0] * 3
    for j in range(n):
        d[a[j] % 3] += 1

    num = 0
    num += d[0]
    k = min(d[1], d[2])
    num += k
    d[1], d[2] = d[1] - k, d[2] - k
    num += d[1] // 3
    num += d[2] // 3
    print(num)
