def solve():
    n, m, k = map(int, input().split())
    c = n // k
    if m < c:
        print(m)
    else:
        print(c - (m - c + k - 2) // (k - 1))


for i in range(int(input())):
    solve()
