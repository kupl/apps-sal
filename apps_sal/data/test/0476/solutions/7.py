def main():
    s = str(input())
    if (s == '1'):
        print("YES")
        return
    if (s == '14'):
        print("YES")
        return
    if (s == '144'):
        print("YES")
        return
    if (s.find('444') != -1):
        print('NO')
        return

    f2 = (s.count('4') + s.count('1')) == len(s)
    f3 = (s.count('1') > 1)
    f4 = (s[0] == '1')
    if (f2 and f3 and f4):
        print("YES")
    else:
        print("NO")


main()
