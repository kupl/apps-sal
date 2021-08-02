def main():
    input()
    zz = [0] * 99992
    for a in map(int, input().split()):
        z, l = 0, []
        for p in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101,
                  103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199,
                  211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313):
            if not a % p:
                l.append(p)
                if z < zz[p]:
                    z = zz[p]
                a //= p
                while not a % p:
                    a //= p
                if a == 1:
                    break
        else:
            l.append(a)
            if z < zz[a]:
                z = zz[a]
        z += 1
        for p in l:
            zz[p] = z
    print(max(zz))


def __starting_point():
    main()


__starting_point()
