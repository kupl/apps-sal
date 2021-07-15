for TT in range(1, int(input()) + 1):
    n = int(input())
    l = sorted(map(int, input().split()))
    k = max(0, min(n - 2, l[-2] - 1))
    print(k)
