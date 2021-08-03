def isMirror(s):
    x = s[::-1]
    if(x != s):
        return False
    n = s.count('A') + s.count('H') + s.count('I') + s.count('M') + s.count('O') + s.count('T') + s.count('U') + s.count('V') + s.count('W') + s.count('X') + s.count('Y')
    if(n != len(s)):
        return False
    return True


s = input()

if(isMirror(s) == True):
    print('YES')
else:
    print('NO')
