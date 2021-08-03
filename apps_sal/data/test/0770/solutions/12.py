def solve():
    n = int(input())
    A = list(map(int, input().split()))
    need = A.count(1)
    k = 0
    ans = 0
    i = 0
    j = 0
    while k != need:
        if j == 0:
            if A[i] == 1:
                A[i] = 0
                j = 1
                ans += 1
                k += 1
            else:
                i += 1
        else:
            if A[i + 1] == 1:
                A[i + 1] = 0
                ans += 1
                k += 1
                i += 1
            else:
                j = 0
                ans += 1
    print(ans)


solve()
