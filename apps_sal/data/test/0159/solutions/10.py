input()


def nod(a, b):
    while b:
        a, b = b, a % b
    return a


def main():
    a = list(map(int, input().split()))
    out = []
    k = 0
    for i in range(0, len(a) - 1):
        out.append(a[i])
        if nod(a[i], a[i + 1]) != 1:
            out.append(1)
            k += 1
    out.append(a[len(a) - 1])
    str_out = " ".join(map(str, out))
    print(k)
    print(str_out)


main()
