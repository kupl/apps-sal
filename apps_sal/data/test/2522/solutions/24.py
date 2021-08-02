
from collections import Counter


def resolve():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    CNT = Counter(A + B)
    num = CNT.most_common()[0][1]
    if num > N:
        print("No")
        return

    j, pre = 0, -1
    for i in range(N):
        if A[i] != pre:
            j = 0
        if A[i] == B[i]:
            while j < N:
                if A[i] != B[j] and A[j] != B[i]:
                    B[i], B[j] = B[j], B[i]
                    break
                j += 1
        pre = A[i]

    print('Yes')
    print(*B)


def __starting_point():
    resolve()


__starting_point()
