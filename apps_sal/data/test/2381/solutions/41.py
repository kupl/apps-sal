def myabs(n):
    n = int(n)
    if n>0:
        return [n,1]
    else:
        return [abs(n),-1]


N,K = map(int,input().split())
A = list(map(myabs, input().split()))
A.sort(reverse=True)
Mod = 10**9+7

def main(n,k,a,mod):
    flag = True
    for i in a:
        if i[1]==1:
            flag = False
            break
    if k%2==0:
        flag = False

    #All elements are negative and odd k
    if flag:
        ans = 1
        for i in range(n-1,n-1-k,-1):
            ans *= (a[i][0]*(-1))%mod
            ans %= mod
        print(ans)
    else:
        ans = [1,1]
        neg_flag = False
        min_neg = -1
        min_pos = -1
        for i in range(k):
            if a[i][1]==-1:
                if neg_flag == True:
                    neg_flag = False
                    ans[1] *= a[i][0]
                    ans[0] = ans[1]
                else:
                    neg_flag = True
                    ans[1] *= a[i][0]
                    min_neg = i
            else:
                ans[0] *= a[i][0]
                ans[1] *= a[i][0]
                min_pos = i
            ans[0] %= mod
            ans[1] %= mod

        if neg_flag and n!=k:
            next_pos = -1
            next_neg = -1
            for i in range(k,n):
                if next_pos==-1 and a[i][1]==1:
                    next_pos = a[i][0]
                elif next_neg==-1 and a[i][1]==-1:
                    next_neg = a[i][0]
                if next_pos>=0 and next_neg>=0:
                    break
            if min_pos==-1:
                ans[0] *= next_pos%mod
                ans[0] %= mod
                print(ans[0])
            elif a[min_neg][0]*next_neg>a[min_pos][0]*next_pos:
                fin_ans = 1
                for i in range(k):
                    if i!=min_pos:
                        fin_ans *= a[i][0]%mod
                        fin_ans %= mod
                fin_ans *= next_neg%mod
                fin_ans %= mod
                print(fin_ans)
            else:
                fin_ans = 1
                for i in range(k):
                    if i!=min_neg:
                        fin_ans *= a[i][0]%mod
                        fin_ans %= mod
                fin_ans *= next_pos%mod
                fin_ans %= mod
                print(fin_ans)
        elif n==k and neg_flag:
            print((ans[1]*-1)%mod)
        else:
            print(ans[1])




def __starting_point():
    main(N,K,A,Mod)
__starting_point()
