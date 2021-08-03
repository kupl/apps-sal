def solve(n):
    even = (n // 2) * (n // 2 + 1)
    odd = ((n + 1) // 2) * ((n + 1) // 2)
    return even - odd


Q = int(input())
for _ in range(Q):
    (l, r) = list(map(int, input().split(' ')))
    ans = solve(r) - solve(l - 1)
    print(ans)
