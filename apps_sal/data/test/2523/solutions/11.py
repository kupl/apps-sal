def main():
    S = input()
    r = len(S)
    if S.count('0') == r:
        return r
    if S.count('1') == r:
        return r
    N = len(S)
    one = S[0] == '1'
    c = 0
    for i in range(N):
        if S[i] == '1' and one or (S[i] == '0' and (not one)):
            continue
        r = min(r, max(i, N - i))
        one = S[i] == '1'
    return r


print(main())
