import sys


def fun():
    try:
        str = input()
    except ValueError:
        print('Invalid number')
        return
    S = {"}": "{", ")": "(", ">": "<", "]": "["}
    L = []
    ans = 0
    for c in str:
        if c in S.values():
            L.append(c)
            pass
        else:
            if(len(L) > 0):
                ans += 0 if S[c] == L.pop() else 1
            else:
                ans = -1
                break
            pass
    if(len(L) > 0 or ans < 0):
        print('Impossible')
    else:
        print(ans)
    pass


def __starting_point():
    fun()
    '''
    for i,v in enumerate(map(int,input().split())):
        print(i,v)
    '''


__starting_point()
