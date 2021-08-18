N = int(input())
A = []
for _ in range(N):
    a = int(input())
    b = []
    for _ in range(a):
        b.append(list(map(int, input().split())))
    A.append(b)


def F(i):
    cnt = 0
    B = [-1] * N
    r = 0
    for j in range(N):
        if (i >> j) & 1:
            r += 1
            if B[j] == 0:
                return 0
            B[j] = 1
            for p, q in A[j]:
                if q == 0:
                    if B[p - 1] == 1:
                        return 0
                    B[p - 1] = 0
                else:
                    if B[p - 1] == 0:
                        return 0
                    B[p - 1] = 1
            else:
                cnt += 1
        else:
            if B[j] == 1:
                return 0
            B[j] = 0

    if cnt == r:
        return cnt


ans = 0
for i in range(1 << N):
    ans = max(ans, F(i))
print(ans)
