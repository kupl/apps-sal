mod = 998244353
maxn = 200002

def pow(a, e):
    if e <= 0: return 1
    
    ret = 1
    while e:
        if e & 1:
           ret = (ret * a) % mod
        a = (a * a) % mod
        e >>= 1
    return ret 



fn, fe = [1], [None]

def build(k):
    fn.append(k-2)
    fe.append(k-1)

    for i in range(2, maxn):
        fe.append( ((k-1) * fn[i-1]) % mod )
        fn.append( ((k-1) * fn[i-2] + (k-2) * fn[i-1]) % mod )





def getRanges(arr):
    q, st, en = [], -1, -1

    for i, x in enumerate(arr):
        if x == -1:
            if st == -1:
                st = en = i
            else:
                en = i
        else:
            if st >= 0:
                q.append((st, en))
                st, en = -1, -1
    if arr[-1] == -1:
        q.append((st, en))

    return q

def getWays(arr, k):
    ans = 1

    for st, en in getRanges(arr):
        if st == 0 and en == len(arr)-1:
            ans *= k * pow(k-1, en-st)
        elif st == 0 or en == len(arr)-1:
            ans *= pow(k-1, en-st+1)
        elif arr[st-1] == arr[en+1]:
            ans *= fe[en-st+1]
        else:
            ans *= fn[en-st+1]
        
        ans %= mod
    
    return ans


def incorrect(arr, n):
    for i in range(1, n-1):
        if arr[i-1] == arr[i+1] and arr[i-1] != -1:
            return True
    return False




def main():
    n, k = list(map(int, input().split()))
    arr = [int(x) for x in input().split()]

    if incorrect(arr, n):
        print(0)
        return

    build(k)

    even = [x for i, x in enumerate(arr) if i & 1 == 0 ]
    odd = [x for i, x in enumerate(arr) if i & 1 == 1 ]

    e, o = getWays(even, k), getWays(odd, k)

    print((e * o) % mod)



def __starting_point():
    main()



__starting_point()
