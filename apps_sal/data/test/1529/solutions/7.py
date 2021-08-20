def main():
    n = int(input())
    (f, r) = (0, 0)
    Sr = "Rainbow's"
    Sf = "Freda's"
    Su = "OMG>.< I don't know!"
    for _ in range(n):
        s = str(input())
        if s.find('miao.') == 0:
            r = 1
        else:
            r = 0
        if s.rfind('lala.') == len(s) - 5:
            f = 1
        else:
            f = 0
        if r and (not f):
            print(Sr)
        elif f and (not r):
            print(Sf)
        elif r and f or (not f and (not r)):
            print(Su)


main()
