t = int(input())
for _ in range(t):
    (n, k) = list(map(int, input().split()))
    if k != 0 and k % 3 == 0:
        extras = (n + 1) // (k + 1)
        n = n - extras
    if n % 3 == 0:
        print('Bob')
    else:
        print('Alice')
