def main():
    n = int(input())
    a = list(map(int,input().split()))
    mod = 10**9+7
    div = {}
    for i in range(61):
        div[i] = 0
    for i in range(n):
        b = bin(a[i])
        l = len(b)
        for j in range(l-2):
            if b[l-1-j]=='1':
                div[j]+=1
    ans = 0
    for k in list(div.keys()):
        ans += div[k] * (n-div[k]) * 2**k
        ans = ans % mod
    print(ans)

def __starting_point():
    main()

__starting_point()
