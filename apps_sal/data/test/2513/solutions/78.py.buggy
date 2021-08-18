import sys
n = int(input())
s = list(input())
l = list(0 for i in range(n))
l[0] = 'S'
l[1] = 'S'
for i in range(1, n - 1):
    if l[i] == 'S':
        if l[i - 1] == 'S':
            if (s[i] == 'o'):
                l[i + 1] = 'S'
            else:
                l[i + 1] = 'W'
        else:
            if s[i] == 'o':
                l[i + 1] = 'W'
            else:
                l[i + 1] = 'S'
    else:
        if l[i - 1] == 'S':
            if (s[i] == 'o'):
                l[i + 1] = 'W'
            else:
                l[i + 1] = 'S'
        else:
            if s[i] == 'o':
                l[i + 1] = 'S'
            else:
                l[i + 1] = 'W'
if l[n - 1] == 'S':
    if l[n - 2] == 'S':
        if (s[n - 1] == 'o'):
            if l[0] == 'S':
                if s[0] == 'o':
                    if l[n - 1] == l[1]:
                        l = ''.join(l)
                        print(l)
                        return
                else:
                    if l[n - 1] != l[1]:
                        l = ''.join(l)
                        print(l)
                        return
        else:
            if l[0] == 'W':
                if s[0] == 'o':
                    if l[n - 1] != l[1]:
                        l = ''.join(l)
                        print(l)
                        return
                else:
                    if l[n - 1] == l[1]:
                        l = ''.join(l)
                        print(l)
                        return
    else:
        if s[n - 1] == 'o':
            if l[0] == 'W':
                if s[0] == 'o':
                    if l[n - 1] != l[1]:
                        l = ''.join(l)
                        print(l)
                        return
                else:
                    if l[n - 1] == l[1]:
                        l = ''.join(l)
                        print(l)
                        return
        else:
            if l[0] == 'S':
                if s[0] == 'o':
                    if l[n - 1] == l[1]:
                        l = ''.join(l)
                        print(l)
                        return
                else:
                    if l[n - 1] != l[1]:
                        l = ''.join(l)
                        print(l)
                        return
else:
    if l[n - 2] == 'S':
        if (s[n - 1] == 'o'):
            if l[0] == 'W':
                if s[0] == 'o':
                    if l[n - 1] != l[1]:
                        l = ''.join(l)
                        print(l)
                        return
                else:
                    if l[n - 1] == l[1]:
                        l = ''.join(l)
                        print(l)
                        return
        else:
            if l[0] == 'S':
                if s[0] == 'o':
                    if l[n - 1] == l[1]:
                        l = ''.join(l)
                        print(l)
                        return
                else:
                    if l[n - 1] != l[1]:
                        l = ''.join(l)
                        print(l)
                        return
    else:
        if s[n - 1] == 'o':
            if l[0] == 'S':
                if s[0] == 'o':
                    if l[n - 1] == l[1]:
                        l = ''.join(l)
                        print(l)
                        return
                else:
                    if l[n - 1] != l[1]:
                        l = ''.join(l)
                        print(l)
                        return
        else:
            if l[0] == 'W':
                if s[0] == 'o':
                    if l[n - 1] != l[1]:
                        l = ''.join(l)
                        print(l)
                        return
                else:
                    if l[n - 1] == l[1]:
                        l = ''.join(l)
                        print(l)
                        return
l[0] = 'S'
l[1] = 'W'
for i in range(1, n - 1):
    if l[i] == 'S':
        if l[i - 1] == 'S':
            if (s[i] == 'o'):
                l[i + 1] = 'S'
            else:
                l[i + 1] = 'W'
        else:
            if s[i] == 'o':
                l[i + 1] = 'W'
            else:
                l[i + 1] = 'S'
    else:
        if l[i - 1] == 'S':
            if (s[i] == 'o'):
                l[i + 1] = 'W'
            else:
                l[i + 1] = 'S'
        else:
            if s[i] == 'o':
                l[i + 1] = 'S'
            else:
                l[i + 1] = 'W'
if l[n - 1] == 'S':
    if l[n - 2] == 'S':
        if (s[n - 1] == 'o'):
            if l[0] == 'S':
                if s[0] == 'o':
                    if l[n - 1] == l[1]:
                        l = ''.join(l)
                        print(l)
                        return
                else:
                    if l[n - 1] != l[1]:
                        l = ''.join(l)
                        print(l)
                        return
        else:
            if l[0] == 'W':
                if s[0] == 'o':
                    if l[n - 1] != l[1]:
                        l = ''.join(l)
                        print(l)
                        return
                else:
                    if l[n - 1] == l[1]:
                        l = ''.join(l)
                        print(l)
                        return
    else:
        if s[n - 1] == 'o':
            if l[0] == 'W':
                if s[0] == 'o':
                    if l[n - 1] != l[1]:
                        l = ''.join(l)
                        print(l)
                        return
                else:
                    if l[n - 1] == l[1]:
                        l = ''.join(l)
                        print(l)
                        return
        else:
            if l[0] == 'S':
                if s[0] == 'o':
                    if l[n - 1] == l[1]:
                        l = ''.join(l)
                        print(l)
                        return
                else:
                    if l[n - 1] != l[1]:
                        l = ''.join(l)
                        print(l)
                        return
else:
    if l[n - 2] == 'S':
        if (s[n - 1] == 'o'):
            if l[0] == 'W':
                if s[0] == 'o':
                    if l[n - 1] != l[1]:
                        l = ''.join(l)
                        print(l)
                        return
                else:
                    if l[n - 1] == l[1]:
                        l = ''.join(l)
                        print(l)
                        return
        else:
            if l[0] == 'S':
                if s[0] == 'o':
                    if l[n - 1] == l[1]:
                        l = ''.join(l)
                        print(l)
                        return
                else:
                    if l[n - 1] != l[1]:
                        l = ''.join(l)
                        print(l)
                        return
    else:
        if s[n - 1] == 'o':
            if l[0] == 'S':
                if s[0] == 'o':
                    if l[n - 1] == l[1]:
                        l = ''.join(l)
                        print(l)
                        return
                else:
                    if l[n - 1] != l[1]:
                        l = ''.join(l)
                        print(l)
                        return
        else:
            if l[0] == 'W':
                if s[0] == 'o':
                    if l[n - 1] != l[1]:
                        l = ''.join(l)
                        print(l)
                        return
                else:
                    if l[n - 1] == l[1]:
                        l = ''.join(l)
                        print(l)
                        return
l[0] = 'W'
l[1] = 'S'
for i in range(1, n - 1):
    if l[i] == 'S':
        if l[i - 1] == 'S':
            if (s[i] == 'o'):
                l[i + 1] = 'S'
            else:
                l[i + 1] = 'W'
        else:
            if s[i] == 'o':
                l[i + 1] = 'W'
            else:
                l[i + 1] = 'S'
    else:
        if l[i - 1] == 'S':
            if (s[i] == 'o'):
                l[i + 1] = 'W'
            else:
                l[i + 1] = 'S'
        else:
            if s[i] == 'o':
                l[i + 1] = 'S'
            else:
                l[i + 1] = 'W'
if l[n - 1] == 'S':
    if l[n - 2] == 'S':
        if (s[n - 1] == 'o'):
            if l[0] == 'S':
                if s[0] == 'o':
                    if l[n - 1] == l[1]:
                        l = ''.join(l)
                        print(l)
                        return
                else:
                    if l[n - 1] != l[1]:
                        l = ''.join(l)
                        print(l)
                        return
        else:
            if l[0] == 'W':
                if s[0] == 'o':
                    if l[n - 1] != l[1]:
                        l = ''.join(l)
                        print(l)
                        return
                else:
                    if l[n - 1] == l[1]:
                        l = ''.join(l)
                        print(l)
                        return
    else:
        if s[n - 1] == 'o':
            if l[0] == 'W':
                if s[0] == 'o':
                    if l[n - 1] != l[1]:
                        l = ''.join(l)
                        print(l)
                        return
                else:
                    if l[n - 1] == l[1]:
                        l = ''.join(l)
                        print(l)
                        return
        else:
            if l[0] == 'S':
                if s[0] == 'o':
                    if l[n - 1] == l[1]:
                        l = ''.join(l)
                        print(l)
                        return
                else:
                    if l[n - 1] != l[1]:
                        l = ''.join(l)
                        print(l)
                        return
else:
    if l[n - 2] == 'S':
        if (s[n - 1] == 'o'):
            if l[0] == 'W':
                if s[0] == 'o':
                    if l[n - 1] != l[1]:
                        l = ''.join(l)
                        print(l)
                        return
                else:
                    if l[n - 1] == l[1]:
                        l = ''.join(l)
                        print(l)
                        return
        else:
            if l[0] == 'S':
                if s[0] == 'o':
                    if l[n - 1] == l[1]:
                        l = ''.join(l)
                        print(l)
                        return
                else:
                    if l[n - 1] != l[1]:
                        l = ''.join(l)
                        print(l)
                        return
    else:
        if s[n - 1] == 'o':
            if l[0] == 'S':
                if s[0] == 'o':
                    if l[n - 1] == l[1]:
                        l = ''.join(l)
                        print(l)
                        return
                else:
                    if l[n - 1] != l[1]:
                        l = ''.join(l)
                        print(l)
                        return
        else:
            if l[0] == 'W':
                if s[0] == 'o':
                    if l[n - 1] != l[1]:
                        l = ''.join(l)
                        print(l)
                        return
                else:
                    if l[n - 1] == l[1]:
                        l = ''.join(l)
                        print(l)
                        return
l[0] = 'W'
l[1] = 'W'
for i in range(1, n - 1):
    if l[i] == 'S':
        if l[i - 1] == 'S':
            if (s[i] == 'o'):
                l[i + 1] = 'S'
            else:
                l[i + 1] = 'W'
        else:
            if s[i] == 'o':
                l[i + 1] = 'W'
            else:
                l[i + 1] = 'S'
    else:
        if l[i - 1] == 'S':
            if (s[i] == 'o'):
                l[i + 1] = 'W'
            else:
                l[i + 1] = 'S'
        else:
            if s[i] == 'o':
                l[i + 1] = 'S'
            else:
                l[i + 1] = 'W'
if l[n - 1] == 'S':
    if l[n - 2] == 'S':
        if (s[n - 1] == 'o'):
            if l[0] == 'S':
                if s[0] == 'o':
                    if l[n - 1] == l[1]:
                        l = ''.join(l)
                        print(l)
                        return
                else:
                    if l[n - 1] != l[1]:
                        l = ''.join(l)
                        print(l)
                        return
        else:
            if l[0] == 'W':
                if s[0] == 'o':
                    if l[n - 1] != l[1]:
                        l = ''.join(l)
                        print(l)
                        return
                else:
                    if l[n - 1] == l[1]:
                        l = ''.join(l)
                        print(l)
                        return
    else:
        if s[n - 1] == 'o':
            if l[0] == 'W':
                if s[0] == 'o':
                    if l[n - 1] != l[1]:
                        l = ''.join(l)
                        print(l)
                        return
                else:
                    if l[n - 1] == l[1]:
                        l = ''.join(l)
                        print(l)
                        return
        else:
            if l[0] == 'S':
                if s[0] == 'o':
                    if l[n - 1] == l[1]:
                        l = ''.join(l)
                        print(l)
                        return
                else:
                    if l[n - 1] != l[1]:
                        l = ''.join(l)
                        print(l)
                        return
else:
    if l[n - 2] == 'S':
        if (s[n - 1] == 'o'):
            if l[0] == 'W':
                if s[0] == 'o':
                    if l[n - 1] != l[1]:
                        l = ''.join(l)
                        print(l)
                        return
                else:
                    if l[n - 1] == l[1]:
                        l = ''.join(l)
                        print(l)
                        return
        else:
            if l[0] == 'S':
                if s[0] == 'o':
                    if l[n - 1] == l[1]:
                        l = ''.join(l)
                        print(l)
                        return
                else:
                    if l[n - 1] != l[1]:
                        l = ''.join(l)
                        print(l)
                        return
    else:
        if s[n - 1] == 'o':
            if l[0] == 'S':
                if s[0] == 'o':
                    if l[n - 1] == l[1]:
                        l = ''.join(l)
                        print(l)
                        return
                else:
                    if l[n - 1] != l[1]:
                        l = ''.join(l)
                        print(l)
                        return
        else:
            if l[0] == 'W':
                if s[0] == 'o':
                    if l[n - 1] != l[1]:
                        l = ''.join(l)
                        print(l)
                        return
                else:
                    if l[n - 1] == l[1]:
                        l = ''.join(l)
                        print(l)
                        return
print((-1))
