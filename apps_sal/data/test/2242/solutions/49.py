def MultipleOf2019():
    S = input()
    s = int(S)
    num, mod, ans = len(S), 2019, 0
    c = [0 for _ in range(num+1)]
    d = [0 for _ in range(mod)]
    d[0] = 1
    s = int(S)
    
    for i in range(num):
        c[i+1] = (c[i]+int(S[-i-1])*pow(10, i, mod))%mod
        d[c[i+1]] += 1

    for i in range(mod):
        ans += d[i]*(d[i]-1)//2
    print(ans)


def __starting_point():
    MultipleOf2019()
    

__starting_point()
