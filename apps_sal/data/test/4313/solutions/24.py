def solve():
    n = int(input())
    v = list(map(int, input().split()))
    c = list(map(int, input().split()))
    res = 0
    for i in range(n):
        x = v[i] - c[i]
        if x > 0:
            res += x
    print(res)

solve()
