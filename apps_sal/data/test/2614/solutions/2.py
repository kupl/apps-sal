T = int(input())
for case in range(T):
    n = int(input())
    a = list(map(int, input().split()))
    sums = {}
    for cake in a:
        if sums.get(cake):
            sums[cake] += 1
        else:
            sums[cake] = 1
    sums = list(sums.values())
    sums.sort()
    m = sums[-1]
    nummax = 0
    for sum in sums:
        if sum == m:
            nummax += 1
    ans = (n - nummax) // (m - 1) - 1
    print(ans)
