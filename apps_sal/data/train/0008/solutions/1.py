import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, k = map(int, input().split())
    s = input()
    s = [s[i] for i in range(n)]

    base = s.count("W")
    if base == 0:
        if k:
            print(2 * k - 1)
        else:
            print(0)
    elif base + k >= n:
        print(2 * n - 1)
    else:
        interval = []
        while s and s[-1] == "L":
            s.pop()
        s = s[::-1]
        while s and s[-1] == "L":
            s.pop()

        while s:
            if s[-1] == "W":
                while s and s[-1] == "W":
                    s.pop()
            else:
                tmp = 0
                while s and s[-1] == "L":
                    s.pop()
                    tmp += 1
                interval.append(tmp)
        interval.sort(reverse=True)
        K = k
        while interval and k:
            if k >= interval[-1]:
                k -= interval.pop()
            else:
                break
        print(2 * (base + K) - 1 - len(interval))
