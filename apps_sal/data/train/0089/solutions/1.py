for _ in range(int(input())):
    N = int(input())
    A = [int(x) for x in input().split()]
    last = i = j = 1
    ans = nxt = cur = 0
    while j < N:
        while j < N - 1 and A[j + 1] > A[j]:
            j += 1
        if cur == 0:
            ans += 1
        nxt += j - i + 1
        j += 1
        i = j
        cur += 1
        if cur == last:
            last = nxt
            nxt = cur = 0

    print(ans)
