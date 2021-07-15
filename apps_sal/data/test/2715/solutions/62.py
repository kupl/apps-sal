#Nを適当にとる
#各a[i](1<=i<=N)に順番に1回ずつ操作を行うことをK//N回繰り返す
#一周する完遂するごとにa[i]は１ずつ減っていく
#自身以外の操作に対して1だけ増加するので、a[i]は合計でK//N*(N-1)+だけ増える.
#したがって、a[i]の初期値はN-1+K//N


def main():
    K = int(input())
    N = 50
    loop, remain = divmod(K, N)
    a = [N-1+loop+N-remain+1 if i < remain else N-1+loop-remain for i in range(N)]
    print(N)
    print((*a))

    
def __starting_point():
    main()

__starting_point()
