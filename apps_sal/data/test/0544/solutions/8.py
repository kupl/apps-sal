def move(c):
    if c == 'a':
        return ['b']
    elif c == 'z':
        return ['y']
    return [chr(ord(c) - 1), chr(ord(c))]


def solve(s):
    l = 0
    r = len(s) - 1
    while l < r:
        d = abs(ord(s[l]) - ord(s[r]))
        if not(d == 0 or d == 2):
            return False
        l += 1
        r -= 1
    return True


n = int(input())
for i in range(n):
    l = input()
    s = input()
    if solve(s):
        print('YES')
    else:
        print('NO')
