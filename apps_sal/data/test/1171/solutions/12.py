def main():
    import copy
    n,k = list(map(int,input().split()))
    v = list(map(int,input().split()))
    ans = 0
    for i in range(min(n+1,k+1)):
        t = v[0:i]
        for j in range(min(n-i+1,k-i+1)):
            t_ = copy.deepcopy(t)
            t_ += v[n-j:n]
            
            r = k-i-j
            t_ = sorted(t_)
            cnt = 0
            for l in range(len(t_)):
                if t_[l]<0 and cnt<r:
                    t_[l] = 0
                    cnt += 1
                else:
                    break
            if ans<sum(t_):
                ans = sum(t_)
    print(ans)

def __starting_point():
    main()

__starting_point()
