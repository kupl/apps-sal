T = int(input())
for _ in range(T):
    n = int(input())
    s = []
    for k in range(n):
        l, r = [int(i) for i in input().split()]
        s.append([l, 1, k])
        s.append([r, 2, k])
    s.sort()
    u = [2] * n
    o = set()
    for i in s:
        u[i[2]] = 1
        if i[2] not in o:
            o.add(i[2])
        else:
            o.remove(i[2])
        if not o:
            if i != s[-1]:
                print(*u)
                break
    else:
        print(-1)
