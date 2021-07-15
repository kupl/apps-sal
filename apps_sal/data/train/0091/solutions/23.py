w = int(input())
for q in range(w):
    fr = 1
    n = int(input())
    a = list(map(int, input().split()))
    a.append(a[0] - 1)
    e = [1] * (n+1)
    ei = 1
    r = [0] * n
    for i in range(n):
        if a[i] == a[i-1]:
            while e[ei] == 0 and ei < n:
                ei += 1
            if ei > a[i]:
                print(-1)
                fr = 0
                break
            r[i] = ei
            e[ei] = 0
        else:
            if e[a[i]] == 1:
                e[a[i]] = 0
                r[i] = a[i]
            else:
                print(-1)
                fr = 0
                break
    if fr:
        print(*r)







