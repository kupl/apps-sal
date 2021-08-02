

def restora(lin):
    lin = lin.split(":")
    ans = []
    falt = 8
    for w in lin:
        if w != "":
            falt -= 1
    for w in lin:
        if w == "":
            while falt > 0:
                ans.append("0000")
                falt -= 1
            continue
        while len(w) < 4:
            w = '0' + w
        ans.append(w)
    return ':'.join(ans)


def main():
    n = int(input())
    for i in range(n):
        print(restora(input()))


main()
