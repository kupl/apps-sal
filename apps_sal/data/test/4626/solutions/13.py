test = int(input())
for _ in range(test):
    ans = 10**10
    a, b, c = map(int, input().split())
    for i in range(-1, 2):
        for j in range(-1, 2):
            for k in range(-1, 2):
                ta = a + i
                tb = b + j
                tc = c + k
                ans = min(ans, abs(ta - tb) + abs(tb - tc) + abs(ta - tc))
    print(ans)
