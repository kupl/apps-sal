import sys
s = input()
k = int(input())


def isPalind(s):
    for i in range(len(s) // 2):
        if s[i] != s[len(s) - 1 - i]:
            return False
    return True


if len(s) % k != 0:
    print('NO')
else:
    l = len(s) // k
    i = 0
    while i < len(s):
        if not isPalind(s[i:i + l]):
            print('NO')
            return
        i += l
    print('YES')
