def readinput():
    s=input()
    return s

def main(s):
    y=int(s[:4])
    m=int(s[5:7])
    d=int(s[9:])
    if m<=4:
        return 'Heisei'
    else:
        return 'TBD'

def __starting_point():
    s=readinput()
    ans=main(s)
    print(ans)

__starting_point()
