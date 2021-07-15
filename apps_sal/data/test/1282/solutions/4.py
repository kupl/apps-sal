s = input()
n = len(s)
try:
    ai = s.index('M')
    bi = n - s[::-1].index('F')
    s = s[ai:bi]
    n = len(s)

    femcount = sum([1 if s == 'F' else 0 for s in s])

    cong = 0
    for a in s:
        if a == 'M':
            cong = max(0, cong - 1)
        else:
            cong += 1

    print(n - femcount + max(0, cong - 1))
except:
    print(0)

# while True:
#     l = list(s)
#     for i in range(len(s) - 1):
#         if s[i] == 'M' and s[i + 1] == 'F':
#             l[i] = 'F'
#             l[i + 1] = 'M'
#     if ''.join(l) == s:
#         break
#     s = ''.join(l)
#     print(s)

