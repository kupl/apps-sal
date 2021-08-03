import sys
input = sys.stdin.readline

t = int(input())
for tests in range(t):
    n = int(input())
    A = list(map(int, input().split()))

    if A[0] < A[-1]:
        print("YES")
    else:
        print("NO")
