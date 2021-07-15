def calc_exp(n):
    return n * ( n + sum(map(int,str(n))) )
    
def binary_search(n):
    l, r = 0, 1<<61
    while (l <= r):
        mid = l+r >> 1
        if (calc_exp(mid) < n):
            l = mid+1
        else:
            r = mid-1
    return l

def main():
    n = int(input())
    res = binary_search(n)
    for i in range(max(1, res-100), res+100):
        if (calc_exp(i) == n):
            print(i)
            return
    print(-1)

main()

