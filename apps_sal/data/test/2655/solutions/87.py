from collections import deque
import sys
read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines


def main():
    n, *a = list(map(int, read().split()))
    a.sort(reverse=True)
    a = deque(a)
    circle_joined = deque()
    next_score = a.popleft()
    r = 0
    flag = False
    while a:
        circle_joined.append(a.popleft())
        if flag:
            next_score = circle_joined.popleft()
            r += next_score
            flag = False
        else:
            r += next_score
            flag = True
    print(r)


def __starting_point():
    main()


__starting_point()
