import heapq


def main():
    N = int(input())
    A = list(map(int, input().split()))
    AH = sorted([(a, i) for i, a in enumerate(A[:2 * N])], reverse=True)
    AT = sorted(A[-N:])
    ATT = []
    for a in AT:
        heapq.heappush(ATT, -a)
    used = [False] * (2 * N)
    for _, i in AH[:N]:
        used[i] = True

    h = sum(a for a, _ in AH[:N])
    t = sum(AT)
    m = h - t
    hp = N
    for i in reversed(list(range(N, 2 * N))):
        t += A[i]
        t += heapq.heappushpop(ATT, -A[i])
        if used[i]:
            h -= A[i]
            while AH[hp][1] > i:
                hp += 1
            h += AH[hp][0]
            used[AH[hp][1]] = True
            hp += 1

        m = max(m, h - t)
    return m


print((main()))
