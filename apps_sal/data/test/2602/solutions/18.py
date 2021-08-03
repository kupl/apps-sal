import sys
input = sys.stdin.readline

t = int(input())
for tests in range(t):
    a, b, n, m = list(map(int, input().split()))

    if min(a, b) >= m and a + b >= n + m:
        print("Yes")
    else:
        print("No")
