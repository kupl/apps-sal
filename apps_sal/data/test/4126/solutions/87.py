s = input()
n = len(s)
flag = False


def palind(S):
    size = len(S)
    for i in range(size // 2):
        if S[i] != S[-1 - i]:
            return False
    return True


if palind(s):
    m = (n - 1) // 2
    sb = s[:m]
    if palind(sb):
        sa = s[m + 1:]
        flag = palind(sa)
print('Yes' if flag else 'No')
