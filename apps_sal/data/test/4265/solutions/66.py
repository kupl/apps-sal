s = input()
t = input()


def counts(s, t):
    cnt = 0
    length = len(s)
    for i in range(length):
        if s[i] != t[i]:
            cnt += 1
    return cnt


print((counts(s, t)))

