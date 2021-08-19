input()
n = input()


def isok(f, s):
    if (f == 'U' or f == 'D') and (s == 'L' or s == 'R'):
        return True
    if (f == 'R' or f == 'L') and (s == 'U' or s == 'D'):
        return True
    return False


first = ''
second = ''
res = 0
for i in range(len(n)):
    if not first:
        first = n[i]
    elif first and (not second):
        if n[i] == first:
            continue
        elif isok(first, n[i]):
            second = n[i]
        else:
            res += 1
            first = n[i]
            second = ''
    elif first and second:
        if n[i] == first or n[i] == second:
            continue
        else:
            res += 1
            first = n[i]
            second = ''
print(res + 1)
