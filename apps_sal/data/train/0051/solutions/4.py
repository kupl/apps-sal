t = int(input())
for l in range(t):
    n, k, d1, d2 = map(int, input().split())
    if n % 3 != 0:
        print("no")
        continue
    n = n // 3
    ok = False
    for i in [-1, 1]:
        for j in [-1, 1]:
            tmp = k;
            tmp -= d1 * i
            tmp -= d1 * i
            tmp -= d2 * j
            if tmp % 3 != 0: continue
            if tmp < 0: continue
            tmp = tmp // 3
            x1 = tmp
            x2 = x1 + d1 * i
            x3 = x2 + d2 * j
            if x1 < 0 or x2 < 0 or x3 < 0: continue
            if x1 <= n and x2 <= n and x3 <= n:
                ok = True
                break
    if ok: print("yes")
    else: print("no")
