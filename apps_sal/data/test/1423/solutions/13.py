def binary_search(l, r, k):
    while (l <= r):
        mid = l+r >> 1
        if (mid < k):
            l = mid+1
        else:
            r = mid-1
    return l

def main():
    n, l, r = map(int, input().split())
    a = list(map(int, input().split()))
    p = list(map(int, input().split()))
    x = [(p[i], i+1, a[i]) for i in range(n)]
    
    x.sort()
    a = [x[i][2] for i in range(n)]
    p = [x[i][1] for i in range(n)]
    b = [0]*(n+1)
    b[p[0]-1] = l
    
    for i in range(1,n):
        idx_list = p[i-1]-1
        b[p[i]-1] = binary_search(l, r, b[idx_list] - a[i-1] + a[i])
        if (b[idx_list] - a[i-1] == b[p[i]-1] - a[i]):
            b[p[i]-1] += 1

    if (max(b) > r):
        print(-1)
        return
    for i in range(n):
        print(b[i], end=' ')

main()
