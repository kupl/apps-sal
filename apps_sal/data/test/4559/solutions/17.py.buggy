import sys

input = sys.stdin.readline
N = int(input())
A = list(map(int, input().split()))

if 0 in A:
    print(0)
else:
    ans = 1
    for a_i in A:
        ans *= a_i
        if ans > 10**18:
            print(-1)
            return
    print(ans)
