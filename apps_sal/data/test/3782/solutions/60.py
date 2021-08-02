import heapq as hp
import sys
input = sys.stdin.readline


def main():
    N, K, Q = map(int, input().split())
    A = list(map(int, input().split()))

    NUM = sorted(list(set(A)))

    ans = 10**10
    for n in NUM:
        Qs = []
        q = []
        for i in range(N):
            if A[i] < n:
                if q:
                    Qs.append(q)
                    q = []
                continue
            if not q:
                q = [A[i]]
            else:
                hp.heappush(q, A[i])
        if q:
            Qs.append(q)
        P = []
        for q in Qs:
            l = len(q)
            if l < K: continue
            for _ in range(min(Q, l - K + 1)):
                v = hp.heappop(q)
                P.append(v)
        if len(P) < Q:
            break
        P.sort()
        ans = min(ans, P[Q - 1] - P[0])
    print(ans)


def __starting_point():
    main()


__starting_point()
