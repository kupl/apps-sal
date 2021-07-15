
def main():
    buf = input()
    n = int(buf)
    buf = input()
    buflist = buf.split()
    a = list(map(int, buflist))

    sublen_inc = []
    sublen_dec = []
    for i in range(n):
        sublen_inc.append(None)
        sublen_dec.append(None)
    c = 1
    sublen_inc[0] = c
    for i in range(1, n):
        if a[i-1] < a[i]:
            c += 1
        else:
            c = 1
        sublen_inc[i] = c
    c = 1
    sublen_dec[n-1] = c
    for i in range(n-2, -1, -1):
        if a[i] < a[i+1]:
            c += 1
        else:
            c = 1
        sublen_dec[i] = c

    best = max(sublen_inc)
    for i in range(1, n-1):
        if a[i-1] < a[i+1]:
            new_sublen = sublen_inc[i-1] + sublen_dec[i+1]
            if new_sublen > best:
                best = new_sublen

    print(best)

def __starting_point():
    main()

__starting_point()
