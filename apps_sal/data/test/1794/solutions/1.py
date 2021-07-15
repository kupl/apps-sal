def main():
    from collections import deque
    n = int(input())
    aa, bb = list(map(int, input().split())), [0] * n
    q, bb[1] = deque([(n - 1, aa.pop())]), 1
    aa.reverse()
    for i, a in enumerate(aa, 2):
        if a == n:
            bb[i] = i
        else:
            lo, hi = 0, len(q)
            while lo <= hi:
                mid = (lo + hi) // 2
                if q[mid][0] > a:
                    lo = mid + 1
                else:
                    hi = mid - 1
            x = q[lo][0]
            bb[i] = x + i + bb[n - x] - a
        while q and q[-1][1] < a:
            del q[-1]
        q.append((n - i, a))
    print(sum(bb))


def __starting_point():
    main()

__starting_point()
