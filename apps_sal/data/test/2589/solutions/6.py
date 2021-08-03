t = int(input())
for i in range(t):
    n, x = map(int, input().split())
    l = [int(i) for i in input().split()]
    cnt = 0
    for i in l:
        if i % x == 0:
            cnt += 1

    if cnt == n:
        print(-1)
    else:
        sm = sum(l)
        if sm % x != 0:
            print(n)
        else:
            ind1 = -1
            ind2 = -1
            for i in range(n):
                if l[i] % x:
                    ind1 = i
                    break
            for i in range(n - 1, -1, -1):
                if l[i] % x:
                    ind2 = i
                    break
            print(max(n - ind1 - 1, ind2))
