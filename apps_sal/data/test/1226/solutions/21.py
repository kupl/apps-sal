#全体の通り数が、2^(N) 通り（全ての花を「選ぶ」「選ばない」の２択）
#したがって、求める値は　2^(N) - 1 - nCa - nCb
#（全体から０本・a本・b本の時を引く）


#全体の通り数 2^(N)をより早く回す関数
def calc_pow(x, y):
    if y == 0:
        return 1

    else:
        ans = calc_pow(x, y//2)**2

        if y%2:
            ans *= x
        
        return ans % 1000000007



#nCa、nCbを求める関数
def calc_combination(n,r,p):
    fact = 1
    factinv = 1
    r = min(r,n-r)

    for i in range(r):
        fact = (fact * (n-i)) % p
        factinv = (factinv * (i+1)) % p
    
    ans = (fact * calc_pow(factinv,p-2)) % p

    return ans

n,a,b = list(map(int,input().split()))
p = 10**9 + 7
ans = (calc_pow(2,n) - calc_combination(n,a,p) - calc_combination(n,b,p)- 1 )%p

print(ans)


 





