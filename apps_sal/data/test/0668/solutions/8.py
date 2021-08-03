n = int(input())
L = list(map(int, input().split()))
if sum(L) < n - 1 or L[0] == 0:
    print(-1)
else:
    print(n - 1)
    count = 1
    M = [True] + [False] * (n - 1)
    while count < n:
        a = 0
        b = 0
        while L[a] == 0 or M[a] == False:
            a += 1
        boltun = -1
        for i in range(1, n):
            if L[i] > boltun and M[i] == False:
                b = i
                boltun = L[i]
        print(a + 1, b + 1)
        L[a] -= 1
        M[b] = True
        count += 1
