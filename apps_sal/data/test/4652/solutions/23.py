for _ in range(int(input())):
    n = int(input())
    p = list(map(int, input().split()))
    i = p.index(1)
    if p[i:] + p[:i] == sorted(p) or p[i + 1:] + p[:i + 1] == sorted(p, reverse=True):
        print("YES")
    else:
        print("NO")
