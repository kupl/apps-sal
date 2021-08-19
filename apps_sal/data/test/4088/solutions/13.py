def main():
    q = int(input())
    for _ in range(q):
        s = input()
        m = int(input())
        t = ["0" for __ in range(m)]
        b = list(map(int, input().split()))
        l = sorted(s)
        d = {}
        for x in s:
            if x in d:
                d[x] += 1
            else:
                d[x] = 1
        while True:
            idxs = []
            num0s = 0
            for c, el in enumerate(b):
                if el == 0:
                    num0s += 1
                    #t[c] = l.pop()
                    idxs.append(c)
                    b[c] = -1
            if not num0s:
                break
            while True:
                chosen = l[-1]
                freq = d[chosen]
                if freq < num0s:
                    l = l[:-freq]
                else:
                    for ix in idxs:
                        t[ix] = chosen
                    l = l[:-freq]
                    break
            for i in range(len(b)):
                for idx in idxs:
                    b[i] -= abs(i - idx)
            # print(b)
        print("".join(t))


main()
