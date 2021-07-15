def main():
    n, k = map(int, input().split())
    inlis = list(map(int, input().split()))
    flag = 0
    trans = 0
    now = 1
    indic = dict()
    indic[1] = 0

    while flag < 1:
        if trans < k:
            trans += 1
            tsugi = inlis[now-1]
            now = tsugi
            if tsugi not in indic:
                indic[tsugi] = trans
                #print(tsugi, indic)
            else:
                flag = 1
                loop = trans - indic[tsugi]
                yokei = indic[tsugi]
                #print(loop, yokei)

        if trans == k:
            print(tsugi)
            return
    
    loopamari = (k-yokei) % loop

    for _ in range(loopamari):
        tsugi = inlis[now-1]
        now = tsugi
    
    print(now)
    




def __starting_point():
    main()
__starting_point()
