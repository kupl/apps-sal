
def YESNO(ans, yes="YES", no="NO"):
    print(([no, yes][ans]))


def II(): return int(input())
def MI(): return list(map(int, input().split()))
def MIL(): return list(MI())
def MIS(): return input().split()


def check(s):
    if s == "":
        return True
    if s[:5] in ["dream", "erase"]:
        return True
    return False


def main():
    S = input()
    i = 0
    l = len(S)
    while i < l:
        if S[i:i + 7] == "dreamer" and check(S[i + 7:]):
            i += 7
        elif S[i:i + 6] == "eraser" and check(S[i + 6:]):
            i += 6
        elif check(S[i:]):
            i += 5
        else:
            return False
    return True


def __starting_point():
    YESNO(main())


__starting_point()
