
def main():
    n, k = map(int,input().split())
    a = list(map(int, input().split()))
    element_count = [0]*1000001
    count=0
    s = 0
    res=0
    for t in range(n):
        element_count[a[t]] += 1
        if element_count[a[t]] == 1: count += 1
        while count > k:
            element_count[a[s]] -= 1
            if element_count[a[s]] == 0: count -= 1
            s +=1
        if t - s + 1 > res:
            res = t - s + 1
            l = s
            r = t
    print(l+1,r+1)


def __starting_point():
    main()
__starting_point()
