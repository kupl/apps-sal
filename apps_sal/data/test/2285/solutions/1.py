for i in range(int(input())):
    t = input().split(':')
    if '' in t:
        j = t.index('')
        t[j: j + 1] = [''] * (9 - len(t))
    print(':'.join(j.rjust(4, '0') for j in t))
