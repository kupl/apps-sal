import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    n = int(input())
    A = list(map(int, input().split()))
    D = {}
    flag = 0
    for i in range(n):
        if A[i] in D:
            D[A[i]].append(i + 1)

        else:
            D[A[i]] = [i + 1]
            flag = flag + 1

    if (flag == 1):
        print("NO")

    else:
        print("YES")

        v = A[0]
        v1 = 0
        for i in range(n):
            if (i + 1 not in D[v]):
                print(D[v][0], i + 1)
                v1 = i + 1

        l = len(D[v])
        for i in range(1, l):
            print(v1, D[v][i])
