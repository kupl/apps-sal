def main():
    input()
    d = {}
    for a in map(int, input().split()):
        z, l = 0, []
        for p in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101,
                  103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199,
                  211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313):
            if not a % p:
                l.append(p)
                x = d.get(p, 0)
                if z < x:
                    z = x
                a //= p
                while not a % p:
                    a //= p
                if a == 1:
                    break
        else:
            l.append(a)
            x = d.get(a, 0)
            if z < x:
                z = x
        d.update(dict.fromkeys(l, z + 1))
    print(max(d.values()))


def __starting_point():
    main()


__starting_point()
