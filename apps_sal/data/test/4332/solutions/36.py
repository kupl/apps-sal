N = int(input())


def S(n):
    s = str(n)
    v = 0
    for i in range(len(s)):
        v += int(s[i])
    return v


print('Yes' if N % S(N) == 0 else 'No')
