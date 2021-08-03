import sys
input = sys.stdin.readline

t = int(input())
for tests in range(t):
    n = int(input())
    A = list(map(int, input().split()))
    print(*sorted(A, reverse=True))
