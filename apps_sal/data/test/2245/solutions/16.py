T = int(input())
for _ in range(T):
    (n, k) = list(map(int, input().split()))
    if k == 3:
        print('Bob' if n % 4 == 0 else 'Alice')
    elif k % 3:
        print('Bob' if n % 3 == 0 else 'Alice')
    else:
        d = n // k % 3
        print('Bob' if n % (k + 1) < k and n % (k + 1) % 3 == 0 else 'Alice')
