n, p = list(map(int, input().split()))
s = input()
slist = list(s)
bad = False
if p == 1:
    print('NO')
    bad = True
if p == 2:
    if s == 'a':
        print('b')
    elif s == 'ab':
        print('ba')
    else:
        print('NO')
    bad = True


def is_palindrome(a):
    if len(a) == 1:
        return False
    return a == list(reversed(a))


def _gen_banned(c, with_c=True):
    nonlocal slist
    banned = []
    if c - 2 >= 0:
        banned.append(ord(slist[c - 2]))
    if c - 1 >= 0:
        banned.append(ord(slist[c - 1]))
    if with_c:
        banned.append(ord(slist[c]))
    return banned


if not bad:
    for c in range(n - 1, -1, -1):
        banned = _gen_banned(c)
        if sorted(banned) == [96 + p - 2, 96 + p - 1, 96 + p]:
            continue
        else:
            #print('huh', c, banned)
            for i in range(ord(slist[c]) + 1, 96 + p + 1):
                if i not in banned:
                    slist[c] = chr(i)
                    break
            if slist[c] == s[c]:
                continue
            j = c + 1
            while j < n:
                banned = _gen_banned(j, with_c=False)
                for i in range(97, 96 + p + 1):
                    if i not in banned:
                        slist[j] = chr(i)
                        break
                j += 1
            print(''.join(slist))
            break
    if ''.join(slist) == s:
        print('NO')
