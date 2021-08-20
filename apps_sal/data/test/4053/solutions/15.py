def f(s):
    X = ''
    k = []
    'for i in L:\n        l = len(i)\n        if s[n-l:] in k:\n            X += "S"\n        elif s[:l] == s[n-l:]:\n            k.append(s[:l])\n            X += "P"\n        else:\n            if s[:l] == i:\n                X += "P"\n                continue\n            if s[n-l:] == i:\n                X += "S"\n                continue\n            return 0\n    if len(X) == 2*n-2:\n        print(X)\n        return 1'
    for i in L:
        l = len(i)
        if l in k:
            if s[:l] == s[n - l:]:
                X += 'S'
            elif s[:l] == i:
                X += 'P'
            elif s[n - l:] == i:
                X += 'S'
            else:
                return 0
        else:
            k.append(l)
            if s[:l] == i:
                X += 'P'
            elif s[n - l:] == i:
                X += 'S'
            else:
                return 0
    print(X)
    return 1


n = int(input())
L = []
for i in range(2 * n - 2):
    L.append(input())
P = sorted(L, key=len)
for i in [P[0], P[1]]:
    for j in [P[2 * n - 3], P[2 * n - 4]]:
        if f(i + j):
            quit()
        if f(j + i):
            quit()
