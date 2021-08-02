S = input()

a1, a2 = -1, -1
for i in range(26):
    t = chr(ord('a') + i)

    s0 = ''
    s1 = ''
    for j, s2 in enumerate(S):
        if s2 == t:
            if s2 == s1:
                a1, a2 = j, j + 1
                break
            elif s2 == s0:
                a1, a2 = j - 1, j + 1
                break
        s0, s1 = s1, s2
    else:
        continue
    break

print((a1, a2))
