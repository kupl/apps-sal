def solve():
    n = int(input())
    a = list(map(int, input().split()))
    if a.count(0) >= n // 2:
        print(n // 2)
        print(' '.join('0' * (n // 2)))
    else:
        m = n // 2
        if m % 2 == 1:
            m += 1
        print(m)
        print(' '.join('1' * (m)))
t = int(input())
for _ in range(t):
    solve()
