import sys
# sys.setrecursionlimit(10**6)
input = sys.stdin.readline
t = int(input())
for t1 in range(t):
    n, k = list(map(int, input().split(" ")))
    if(n >= k):
        if((n + k) % 2 == 0):
            print(0)
        else:
            print(1)
    else:
        print(k - n)
