from collections import deque


def main():
    (n, k) = map(int, input().split())
    s = input()
    t = []
    t.append(s[0])
    x = s[0]
    for i in range(1, n):
        if x != s[i]:
            t.append(s[i])
            x = s[i]
    j = 0
    t = deque(t)
    while j < k:
        if len(t) <= 2:
            print(n - 1)
            return
        t.popleft()
        t.popleft()
        j += 1
    print(n - 1 - (len(t) - 1))


def __starting_point():
    main()


__starting_point()
