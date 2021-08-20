t = int(input())
for case in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    n_odd = 0
    n_even = 0
    for i in arr:
        if i % 2 == 0:
            n_even += 1
        else:
            n_odd += 1
    if n_even and n_odd:
        print('NO')
    else:
        print('YES')
