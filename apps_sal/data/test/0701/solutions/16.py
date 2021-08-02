def isAuto(s, t):
    j = 0
    for i in range(len(s)):
        if s[i] == t[j]: j += 1
        if j == len(t):
            return True
    return False


def isArray(s, t):
    sarr = [0] * 256
    tarr = [0] * 256
    for i in range(len(s)): sarr[ord(s[i])] += 1
    for i in range(len(t)): tarr[ord(t[i])] += 1
    for i in range(256):
        if sarr[i] != tarr[i]:
            return False
    return True


def isBoth(s, t):
    sarr = [0] * 256
    tarr = [0] * 256
    for i in range(len(s)): sarr[ord(s[i])] += 1
    for i in range(len(t)): tarr[ord(t[i])] += 1
    for i in range(256):
        if sarr[i] < tarr[i]:
            return False
    return True


s = input()
t = input()
if isAuto(s, t):
    print("automaton")
elif isArray(s, t):
    print("array")
elif isBoth(s, t):
    print("both")
else:
    print("need tree")
