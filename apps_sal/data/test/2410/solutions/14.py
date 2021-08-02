def ma(a, size):

    max_so_far = - 10**9
    max_ending_here = 0

    for i in range(0, size):
        max_ending_here = max_ending_here + a[i]
        if (max_so_far < max_ending_here):
            max_so_far = max_ending_here

        if max_ending_here < 0:
            max_ending_here = 0
    return max_so_far


for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    k = ma(a[1:], len(a) - 1)
    j = ma(a[:n - 1], len(a) - 1)
    if sum(a) > max(j, k):
        print('YES')
    else:
        print('NO')
