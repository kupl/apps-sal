def main():
    S = input()
    p = ''
    pp = ''
    for i, s in enumerate(S):
        if p == s:
            return (i, i + 1)
        if pp == s:
            return (i - 1, i + 1)
        pp, p = p, s
    return (-1, -1)


print((*main()))
