def Left(a):
    if (a != 1 and a != 4 and a != 7 and a != 0):
        return True
    return False


def Right(a):
    if (a != 3 and a != 6 and a != 9 and a != 0):
        return True
    return False


def Up(a):
    if (a != 1 and a != 2 and a != 3):
        return True
    return False


def Down(a):
    if (a != 7 and a != 9 and a != 0):
        return True
    return False


n = int(input())
str1 = input()

u = 0
d = 0
l = 0
r = 0
for iss in str1:
    i = int(iss)
    if (Up(i)):
        u += 1
    if (Down(i)):
        d += 1
    if (Left(i)):
        l += 1
    if (Right(i)):
        r += 1

if (u == len(str1)
    or d == len(str1)
    or l == len(str1)
        or r == len(str1)):
    print("NO")
else:
    print("YES")
