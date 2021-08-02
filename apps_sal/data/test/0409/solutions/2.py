def ok(s, a, b):
    indexa = s.find(a)
    if indexa == -1:
        return False
    return s.find(b, indexa + 2) != -1


def __starting_point():
    s = input().strip()
    if ok(s, "AB", "BA") or ok(s, "BA", "AB"):
        print("YES")
    else:
        print("NO")


__starting_point()
