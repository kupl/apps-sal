for __ in range(int(input())):
    (n, k, d) = list(map(int, input().split()))
    ar = list(map(int, input().split()))
    A = dict()
    num = 0
    for i in range(d):
        if ar[i] in A:
            A[ar[i]] += 1
        else:
            A[ar[i]] = 1
            num += 1
    ans = num
    for j in range(d, n):
        A[ar[j - d]] -= 1
        if A[ar[j - d]] == 0:
            num -= 1
        if ar[j] in A:
            if A[ar[j]] == 0:
                num += 1
            A[ar[j]] += 1
        else:
            A[ar[j]] = 1
            num += 1
        ans = min(num, ans)
    print(ans)
