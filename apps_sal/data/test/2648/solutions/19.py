from collections import Counter

N = int(input())
A = list(map(int, input().split()))

C = Counter(A)
C = sorted(C.items())

cc = []
for a, b in C:
    cc.append([a, b])
C = cc

M = len(C)

left = 0
right = M - 1

while True:
    if C[left][1] < 2:
        p_left = left
        for left in range(p_left, M):
            if C[left][1] > 1:
                break

    if C[right][1] < 2:
        p_right = M - right - 1
        for right in range(M):
            if C[M - right - 1][1] > 1:
                break

        right = M - right - 1

    if C[left][1] <= 1 and C[right][1] <= 1:
        break

    if left == right:
        if C[left][1] >= 3:
            C[left][1] -= 2
        else:
            f = 0
            C[left][1] -= 1
            for i in range(left + 1, M):
                if C[i][1] > 0:
                    C[i][1] -= 1
                    f = 1
                    break

            if f == 0:
                for i in range(0, left):
                    if C[i][1] > 0:
                        C[i][1] -= 1

    else:
        C[left][1] -= 1
        C[right][1] -= 1


ans = 0
for a, b in C:
    ans += b

print(ans)
