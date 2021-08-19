for TT in range(1, int(input()) + 1):
    n = int(input())
    l = sorted(map(int, input().split()), reverse=True)
    print(max((min(i + 1, l[i]) for i in range(n))))
