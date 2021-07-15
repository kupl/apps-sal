import sys
input = sys.stdin.readline


t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    ru = [0] * (n + 1)
    ans = 0
    for i in range(n):
        if i % 2 == 0:
            ans += a[i]
            ru[i + 1] = ru[i] - a[i]
        else:
            ru[i + 1] = ru[i] + a[i]

    li1 = [0]
    li2 = [0]
    for i in range(n):
        if i % 2 == 0:
            li1.append(ru[i + 1])
        else:
            li2.append(ru[i + 1])

    add = 0
    min_val = 0
    for val in li1:
        add = max(val - min_val, add)
        min_val = min(min_val, val)

    min_val = 0
    for val in li2:
        add = max(val - min_val, add)
        min_val = min(min_val, val)

    print(ans + add)
