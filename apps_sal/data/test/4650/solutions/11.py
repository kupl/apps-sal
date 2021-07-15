q = int(input())
for _ in range(q):
    n = int(input())
    u = list(map(int, input().split()))
    a0, a1, a2 = [0, 0, 0]
    for i in range(n):
        if u[i] % 3 == 0:
            a0 += 1
        elif u[i] % 3 == 1:
            a1 += 1
        else:
            a2 += 1
    w1 = a0 + min(a1, a2)
    w2 = min(a1, a2)
    a1 -= w2; a2 -= w2
    w1 += a1 // 3 + a2 // 3
    print(w1)
    

