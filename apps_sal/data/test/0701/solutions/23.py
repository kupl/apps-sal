def f(a, b):
    j, n = 0, len(b)
    for i in a:
        if i == b[j]:
            j += 1
            if j == n: return True
    return False
a, b = input(), input()
t = [0] * 26
for i in a: t[ord(i) - 97] += 1
for i in b: t[ord(i) - 97] -= 1
if any(i < 0 for i in t): print('need tree')
elif len(b) == len(a): print('array')
elif f(a, b): print('automaton')
else: print('both')
