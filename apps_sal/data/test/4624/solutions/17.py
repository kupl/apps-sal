import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n, x = list(map(int, input().split()))

    flag = 1
    for i in range(2, n, x):
        flag = flag + 1

    print(flag)
