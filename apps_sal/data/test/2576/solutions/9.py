import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    (a, b, c, d) = list(map(int, input().split()))
    print(max(a + b, c + d))
