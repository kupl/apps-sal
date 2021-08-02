def main():
    N = int(input())
    s = input()
    # 0 sheep 1 wolf
    for i in [[0, 0], [0, 1], [1, 0], [1, 1]]:
        t = i[:]
        for j in s[1:]:
            if t[-1] == 0:
                if j == 'o':
                    t.append(t[-2])
                else:
                    t.append(1 - t[-2])
            elif j == 'o':
                t.append(1 - t[-2])
            else:
                t.append(t[-2])
        if t[-1] == t[0]:
            if s[0] == 'o' and t[0] == 0 and t[1] != t[-2]:
                continue
            if s[0] == 'o' and t[0] == 1 and t[1] == t[-2]:
                continue
            if s[0] == 'x' and t[0] == 0 and t[1] == t[-2]:
                continue
            if s[0] == 'x' and t[0] == 1 and t[1] != t[-2]:
                continue
            print((''.join(['S' if i == 0 else 'W' for i in t[:-1]])))
            return
    print((-1))
    return


main()
