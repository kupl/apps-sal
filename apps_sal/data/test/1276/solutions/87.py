def main():
    N = int(input())
    S = input()
    RGBdict = {'R': 0, 'G': 0, 'B': 0}
    for i in range(N):
        RGBdict[S[i]] += 1
    if N % 2 == 0:
        maxsa = N // 2 - 1
    else:
        maxsa = N // 2
    tmp = N - 2
    cnt = 0
    for j in range(maxsa + 1):
        num = tmp - j * 2
        for k in range(num):
            if S[N - num + k] != S[N - num + k - j - 1] and S[N - num + k] != S[N - num + k - 2 * j - 2] and (S[N - num + k - j - 1] != S[N - num + k - 2 * j - 2]):
                cnt += 1
    ans = RGBdict['R'] * RGBdict['G'] * RGBdict['B']
    ans -= cnt
    return ans


print(main())
