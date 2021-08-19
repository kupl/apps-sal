import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    (n, m) = list(map(int, input().split()))
    print(n ^ m)
