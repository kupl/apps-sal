def solve():
    N = int(input())

    A = [int(k) for k in input().split()]
    A.sort()

    B = [A[0]]
    C = []

    cnt = 1

    for i in range(1, N):
        if A[i] == A[i - 1]:
            cnt += 1
            if cnt > 2:
                print("NO")
                return
        else:
            cnt = 1

        if B[-1] != A[i]:
            B.append(A[i])
        else:
            C.append(A[i])

    print("YES")
    print(len(B))
    print(' '.join(str(k) for k in B))
    print(len(C))
    print(' '.join(str(k) for k in reversed(C)))


def __starting_point():
    solve()


__starting_point()
