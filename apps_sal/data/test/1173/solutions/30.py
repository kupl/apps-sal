from collections import deque


def main():
    N = int(input())
    A = [deque(int(a) - 1 for a in input().split()) for _ in range(N)]

    P, W = [0] * N, [-1] * N
    c = deque(list(range(N)))

    while c:
        i = c.popleft()
        j = A[i].popleft()
        W[i] = j

        if W[j] == i:
            P[i] = P[j] = max(P[i], P[j]) + 1
            if A[i]:
                c.append(i)
            if A[j]:
                c.append(j)

    print((-1 if any(len(a) for a in A) else max(P)))


main()
