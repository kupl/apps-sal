import sys
a = input()
i = 0
while i < len(a):
    if a[i] == '"':
        end = a.index('"', i + 1)
        print('<', a[i + 1:end], '>', sep='')
        i = end + 1
    elif a[i] != ' ' != '"' and (a[i - 1] == ' ' or i - 1 < 0):
        try:
            end = a.index(' ', i + 1)
        except:
            end = len(a)
        print('<', a[i:end], '>', sep='')
        i = end + 1
    else:
        i += 1
