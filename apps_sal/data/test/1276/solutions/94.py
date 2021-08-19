def main():
    N = int(input())
    S = input()
    dict = {'R': 0, 'B': 0, 'G': 0}
    for i in range(N):
        dict[S[i]] += 1
    ans = dict['R'] * dict['B'] * dict['G']
    for i in range(N - 2):
        if (N - i) % 2 == 0:
            tmp = int((N - i) / 2) - 1
        else:
            tmp = (N - i) // 2
        for j in range(1, tmp + 1):
            if S[i] != S[i + j] and S[i] != S[i + 2 * j] and (S[i + j] != S[i + 2 * j]):
                ans = ans - 1
    return ans


print(main())
