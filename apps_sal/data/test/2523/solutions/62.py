def main():
    S = input()
    A = []
    i, t = 1, S[0]
    for s in S[1:]:
        if s != t:
            A.append(i)
            i = 1
            t = s
        else:
            i += 1
    A.append(i)

    m, l  = len(S), 0
    for a in A:
        t = max(l + a, len(S) - l - a)
        m = min(m, t)
        l += a
    return m

print((main()))

