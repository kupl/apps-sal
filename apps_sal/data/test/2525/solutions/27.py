
from collections import deque


def main():
    s = deque(input())
    q = int(input())
    flg = 0

    for i in range(q):
        l = list(map(str, input().split()))
        if len(l) == 1:
            flg = 1 - flg
        elif (flg == 0 and l[1] == "1") or (flg == 1 and l[1] == "2"):
            s.appendleft(l[2])
        else:
            s.append(l[2])

    if flg == 0:
        print(("".join(s)))
    else:
        print(("".join(reversed(s))))


main()

