def test(m):
    t = [i for i in range(2**m)]
    for i in range(2**m):
        t.append(i)
    t.sort()
    st = set()
    bt = set()
    from itertools import permutations
    for v in permutations(t):
        taget = v[0]
        x = 0
        idx = 1
        while idx < len(v) and v[idx] != taget:
            x = x ^ v[idx]
            idx += 1
        if x in st or x in bt:
            continue
        f = True
        for i in range(1, len(v)):
            g = False
            y = 0
            idx = i + 1
            while idx < len(v):
                if v[i] == v[idx]:
                    g = True
                    break
                y = y ^ v[idx]
                idx += 1
            if g:
                if y != x:
                    f = False
                    break
        if f:
            st.add(x)
            print(x, v)


def main():
    m, k = map(int, input().split())
#    test(m)
    x = 0
    for i in range(2**m):
        if i == k:
            continue
        x ^= i
    if k == 0:
        for i in range(2**m):
            print(i, i, end=" ")
    elif x == k:
        for i in range(2**m):
            if i == k:
                continue
            print(i, end=" ")
        print(k, end=" ")
        for i in reversed(range(2**m)):
            if i == k:
                continue
            print(i, end=" ")
        print(k)
    else:
        print(-1)


def __starting_point():
    main()


__starting_point()
