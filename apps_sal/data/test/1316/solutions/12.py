from sys import stdin


def kmp(pat, txt):
    leng = 0
    i = 1
    ans = 0
    M = len(pat)
    N = len(txt)
    lps = [0] * M
    j = 0
    # Calculo de lps, prefifo propio mas largo que tambien es sufijo de pat[0:i]
    while i < M:
        if pat[i] == pat[leng]:
            leng += 1
            lps[i] = leng
            i += 1
        elif leng != 0:
            leng = lps[leng - 1]
        else:
            lps[i] = 0
            i += 1
    i = 0
    while i < N:

        if pat[j] == txt[i]:
            i += 1
            j += 1
        if j == M:
            ans += 1
            i = i - j + len(pat)
            j = 0
        elif i < N and pat[j] != txt[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return ans


n, m = list(map(int, stdin.readline().strip().split()))
s = stdin.readline().strip()
ans = 0
for i in range(26):
    ans = max(ans, kmp(chr(97 + i) * m, s))
print(ans)
