s = input()
s1 = s[::-1]
p = False


def try1(a):
    q = s[:a] + s1[a] + s[a::]
    q1 = q[::-1]
    for i in range(a + 1, len(q) // 2):
        if q[i] != q1[i]:
            return False
    return True


def try2(a):
    q = s[:len(s) - a] + s[a] + s[len(s) - a::]
    q1 = q[::-1]
    for i in range(a + 1, len(q) // 2):
        if q[i] != q1[i]:
            return False
    return True


for i in range(len(s) // 2):
    if s[i] != s1[i]:
        if try1(i):
            q = s[:i] + s1[i] + s[i::]
            print(q)
            return
        elif try2(i):
            q = s[:len(s) - i] + s[i] + s[len(s) - i::]
            print(q)
            return
        else:
            p = True
            break
if p:
    print("NA")
else:
    d = s[:len(s) // 2] + s[len(s) // 2] + s[len(s) // 2::]
    print(d)
