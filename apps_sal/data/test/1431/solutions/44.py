def main():
    n = int(input())
    a = list(map(int,input().split()))
    ans = [-1 for i in range(n)]
    for i in range(n):
        c = n//(n-i)
        if c<2:
            if a[n-1-i] == 1:
                ans[n-1-i] = 1
            else:
                ans[n-1-i] = 0
        else:
            s = 0
            for j in range(2,c+1):
                s += ans[j*(n-i)-1]
            ans[n-i-1] = (s+a[n-1-i])%2 
    a = []
    for i in range(n):
        if ans[i] == 1:
            a.append(i+1)
    if len(a)==0:
        print((0))
    else:
        print((len(a)))
        print((' '.join(list(map(str,a)))))

def __starting_point():
    main()

__starting_point()
