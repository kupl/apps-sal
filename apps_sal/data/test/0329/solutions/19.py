def v_19(s):
    a = [0, 0, 0, 0]
    #    n  e  i  t

    for i in range(len(s)):
        if s[i] == 'n':
            a[0] += 1
        elif s[i] == 'i':
            a[2] += 1
        elif s[i] == 'e':
            a[1] += 1
        elif s[i] == 't':
            a[3] += 1

    return a


s = input()

q = v_19(s)

if q[0] < 5:
    q[0] = q[0] // 3
else:
    q[0] = (q[0] - 1) // 2

q[1] = q[1] // 3

print(min(q))

# 1502218585911

