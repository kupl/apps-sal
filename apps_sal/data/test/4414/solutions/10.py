import sys
input = sys.stdin.readline

q = int(input())

for testcases in range(q):
    a, b, n, S = list(map(int, input().split()))

    x = S // n

    S -= min(x, a) * n

    if S <= b:
        print("YES")
    else:
        print("NO")
