def true_array(b):
    for i in range(len(b)):
        if b[i] == 0:
            return 0
    return 1


t = int(input())
for q in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = [0 for i in range(n)]
    t = 0
    while true_array(b) != 1:
        for m in a:
            for i in range(max(m - t - 1, 0), min(m + t, n)):
                b[i] = 1
        t += 1
    print(t)
