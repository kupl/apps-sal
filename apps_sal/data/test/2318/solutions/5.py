def getN():
    return int(input())
def getList():
    return list(map(int, input().split()))

def solve():
    first = input()
    second = input()
    fbuf = []
    sbuf = []
    fcur = "0"
    scur = "0"
    for c in first:
        if fcur[-1] != c:
            fbuf.append(fcur)
            fcur = c
        else:
            fcur += c
    fbuf.append(fcur)

    for c in second:
        if scur[-1] != c:
            sbuf.append(scur)
            scur = c
        else:
            scur += c
    sbuf.append(scur)

    # print(fbuf, sbuf)
    if len(fbuf) != len(sbuf):
        print("NO")
        return

    for f, s in zip(fbuf, sbuf):
        if f[0] != s[0]:
            print("NO")
            return

        if len(f) > len(s):
            print("NO")
            return

    print("YES")
    return


n = getN()

for i in range(n):
    solve()
