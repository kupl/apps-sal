t = int(input())
for i in range(t):
    (n, k) = list(map(int, input().split()))
    if k % 3 != 0 or k > n:
        print('Bob' if n % 3 == 0 else 'Alice')
    else:
        print('Bob' if n % (k + 1) % 3 == 0 and n % (k + 1) != k else 'Alice')
