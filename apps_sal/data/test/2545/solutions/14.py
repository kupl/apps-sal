import sys
input = sys.stdin.readline

t = int(input())

for testcases in range(t):
    a, b = list(map(int, input().split()))

    if a > 2 * b or b > 2 * a:
        print("NO")

    else:
        if (a + b) % 3 == 0:
            print("YES")
        else:
            print("NO")
