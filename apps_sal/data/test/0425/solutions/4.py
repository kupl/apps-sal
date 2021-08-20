def Dec_to_Bin(N):
    b = ''
    while N > 0:
        b = str(N % 2) + b
        N = N // 2
    if b == '':
        return '0'
    return b


if True:
    (n, p) = list(map(int, input().split()))
    j = 1
    while True:
        if n - p * j <= 0:
            print(-1)
            break
        S = Dec_to_Bin(n - p * j)
        if S.count('1') <= j:
            ans = 0
            k = 0
            while k < len(S):
                ans += int(S[k]) * 2 ** (len(S) - k - 1)
                k += 1
            if ans >= j:
                print(j)
            else:
                print(-1)
            break
        j += 1
