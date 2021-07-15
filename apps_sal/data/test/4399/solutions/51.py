def readinput():
    s=input()
    return s

def main(s):
    if s == 'AAA' or s == 'BBB':
        return 'No'
    else:
        return 'Yes'

def __starting_point():
    s=readinput()
    ans=main(s)
    print(ans)

__starting_point()
