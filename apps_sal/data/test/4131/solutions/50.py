def main():
    import sys
    input = sys.stdin.readline
    
    N,M = map(int,input().split())
    PY = [[i]+list(map(int,input().split())) for i in range(M)]

    PY = sorted(PY,key = lambda x:(x[1],x[2]))
    
    ans_li = ['0'*12]*M
    town_dict = {}

    for idx,p,y in PY:
        x = town_dict.get(p,1)

        id_ = ('{:6d}'.format(p)+'{:6d}'.format(x)).replace(' ','0')
        ans_li[idx] = id_

        town_dict[p] = town_dict.get(p,1)+1

    print('\n'.join(ans_li))
    
def __starting_point():
    main()
__starting_point()
