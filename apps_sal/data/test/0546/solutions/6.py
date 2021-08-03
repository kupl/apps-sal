good = input()
mask = input()
flag = 0
if '*' in mask:
    flag = 1


def check(a, b):
    if a == b:
        return 1
    if a == '?':
        for i in range(len(good)):
            if good[i] == b:
                return 1
    return 0


n = int(input())
for i in range(n):
    s = input()
    accept = 1
    if not flag:
        if len(s) != len(mask):
            print('NO')
            continue
        for j in range(len(s)):
            if not check(mask[j], s[j]):
                accept = 0
        if not accept:
            print("NO")
        else:
            print("YES")
    else:
        if len(mask) - 1 > len(s):
            print("NO")
            continue
        for j in range(len(mask)):
            if mask[j] != '*':
                if not check(mask[j], s[j]):
                    accept = 0
                    break
            else:
                l = j
                break
        for j in range(len(s)):
            ind = len(mask) - 1 - j
            cur = len(s) - 1 - j
            if mask[ind] != '*':
                if not check(mask[ind], s[cur]):
                    accept = 0
                    break
            else:
                r = cur
                break
        if not accept:
            print('NO')
            continue
        if (len(s) + 1 == len(mask)):
            print('YES')
            continue
        for j in range(l, r + 1):
            for k in range(len(good)):
                if (good[k] == s[j]):
                    accept = 0
        if not accept:
            print('NO')
        else:
            print('YES')
