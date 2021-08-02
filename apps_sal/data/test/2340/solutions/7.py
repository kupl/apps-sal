q = int(input())
for i in range(q):
    h, n = map(int, input().split())
    p = list(map(int, input().split()))
    used = [0]
    for i in range(1, n):
        if i == 1:
            used.append(1)
        else:
            if p[i] >= 1:
                var = 10000000000000
                if p[i - 1] - p[i] == 1:
                    used.append(used[i - 2])
                else:
                    used.append(used[i - 1] + 1)
    i = n - 1
    ans = 0
    if p[i] > 2:
        print(used[-1])
    else:
        if n >= 2 and p[i] == 1:
            print(min(used[-2], used[-1]))
        else:
            print(used[-1])
