def k(s):
    n = (8, -1, -1, 3, 6, 9, 4, 7, 0, 5)
    for i in range(len(s)):
        if n[int(s[i])] != int(s[len(s) - i - 1]):
            return False
    return True


s = input()
if k(s):
    print('Yes')
else:
    print('No')
