s = input()
t = input()


def char_list(s):
    l = [0] * 26
    for x in s:
        i = ord(x) - ord('a')
        l[i] += 1
    l.sort()
    return l


l1 = char_list(s)
l2 = char_list(t)
if l1 == l2:
    print('Yes')
else:
    print('No')
