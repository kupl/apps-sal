def main():
    n = int(input())
    strings = [None] * n
    for i in range(n):
        strings[i] = input()
    print(solver(strings))


def solver(L):
    L.sort(key=cmp_to_key(customCompare))
    return ''.join(L)


def customCompare(x, y):
    a = x + y
    b = y + x
    if a < b:
        return -1
    elif a == b:
        return 0
    else:
        return 1
    # if len(x) == len(y):
    # 	return compareStrings(x, y)
    # elif isPrefix(x, y):
    # 	return compareStrings(x, y[len(x):])
    # elif isPrefix(y, x):
    # 	return compareStrings(x[len(y):], y)
    # else:
    # 	return compareStrings(x, y)


def compareStrings(x, y):
    if x < y:
        return -1
    elif x == y:
        return 0
    else:
        return 1


def isPrefix(s, t):
    if s == t[:len(s)]:
        return True


def cmp_to_key(mycmp):
    class K:
        def __init__(self, obj, *args):
            self.obj = obj

        def __lt__(self, other):
            return mycmp(self.obj, other.obj) < 0

        def __gt__(self, other):
            return mycmp(self.obj, other.obj) > 0

        def __eq__(self, other):
            return mycmp(self.obj, other.obj) == 0

        def __le__(self, other):
            return mycmp(self.obj, other.obj) <= 0

        def __ge__(self, other):
            return mycmp(self.obj, other.obj) >= 0

        def __ne__(self, other):
            return mycmp(self.obj, other.obj) != 0
    return K

# L = ["abba", "abacaba", "bcd", "er"]
# print(solver(L))

# L2 = ['x', 'xx', 'xxa', 'xxaa', 'xxaaa']
# print(solver(L2))

# L3 = ['c', 'cb', 'cba']
# print(solver(L3))


main()
