t = int(input())
for i in range(0, t):
    n = int(input())
    data = list(map(int, input().split()))
    d = dict()
    for j in range(0, n):
        a = data[j]
        count = 0
        while a % 2 == 0:
            a = a // 2
            count += 1
        d[a] = max(d.get(a, 0), count)
    print(sum(d.values()))
