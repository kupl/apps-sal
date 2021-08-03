def main():
    s = input()
    if len(set(s)) == 0 and list(set(s))[0] == 'x':
        return s
    else:
        l = list(s)
        for i in range(len(l)):
            if l[i] != 'x':
                l[i] = 'x'
        return "".join(str(v) for v in l)


def __starting_point():
    print((main()))


__starting_point()
