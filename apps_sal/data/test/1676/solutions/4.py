def main():
    from collections import deque
    a = deque()
    (n, b) = map(int, input().split())
    next_t = 0
    for i in range(n):
        (c, lo) = map(int, input().split())
        while a and a[0] <= c:
            a.popleft()
        if len(a) > b:
            print(-1, end=' ')
        else:
            print(max(next_t, c) + lo, end=' ')
            next_t = max(next_t, c) + lo
            a.append(next_t)


main()
