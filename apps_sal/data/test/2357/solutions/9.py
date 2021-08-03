T = int(input())

for t in range(T):
    n = int(input())

    A = list(map(int, input().split()))

    if n < 2:
        print(-1)

    elif len(set(A)) == n:
        print(-1)

    else:
        M = {a: [] for a in A}

        for i in range(n):
            M[A[i]].append(i)

        ans = n

        for x in M:
            if len(M[x]) > 1:
                for i in range(1, len(M[x])):
                    ans = min(ans, M[x][i] - M[x][i - 1] + 1)

        print(ans)
