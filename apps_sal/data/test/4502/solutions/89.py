from collections import deque
import sys


stdin = sys.stdin
def ns(): return stdin.readline().rstrip()
def ni(): return int(stdin.readline().rstrip())
def nm(): return list(map(int, stdin.readline().split()))
def nl(): return list(map(int, stdin.readline().split()))


def main():
    n = ni()
    A = nl()
    A = deque(A)
    B = deque()
    if n % 2 == 0:
        while A:
            B.append(A.popleft())
            B.appendleft(A.popleft())
        B = list(B)
        print((*B))
    else:
        while len(A) != 1:
            B.append(A.popleft())
            B.appendleft(A.popleft())
        B.append(A.popleft())
        B = list(B)[::-1]
        print((*B))


def __starting_point():
    main()


__starting_point()
