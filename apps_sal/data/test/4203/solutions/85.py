def isAC(S):
    if S[0] != 'A':
        return False
    if S[2:-1].count('C') != 1:
        return False
    S = S[1:].replace('C', '')
    if not all(('a' <= x <= 'z' for x in S)):
        return False
    return True


print('AC' if isAC(input()) else 'WA')
