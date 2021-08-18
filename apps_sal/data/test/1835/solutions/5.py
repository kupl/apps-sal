import sys
input = sys.stdin.readline

Q = int(input())

for test in range(Q):

    n = int(input())
    S = [input().strip() for i in range(n)]

    zero = 0
    lenflag = 0

    for s in S:
        zero += s.count("0")

        if len(s) % 2 == 1:
            lenflag = 1

    if lenflag == 1:
        print(n)
    else:
        if zero % 2 == 0:
            print(n)
        else:
            print(n - 1)
