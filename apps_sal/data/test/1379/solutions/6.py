from collections import deque


def main():
    (n, m, d) = list(map(int, input().split()))
    aa = list(map(int, input().split()))
    (q, cnt) = (deque(((-d, 1),)), 1)
    for i in sorted(list(range(n)), key=aa.__getitem__):
        a = aa[i]
        (b, j) = q.popleft()
        if a <= b + d:
            q.appendleft((b, j))
            j = cnt = cnt + 1
        aa[i] = j
        q.append((a, j))
    print(cnt)
    print(' '.join(list(map(str, aa))))


def __starting_point():
    main()


__starting_point()
