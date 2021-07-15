def resolve():
    n,k,q = map(int,input().split())
    ans = [0]*n
    for _ in range(q):
        a = int(input())
        ans[a-1] += 1
    for i in ans:
        if 0 < k-q+i:
            print('Yes')
        else:
            print('No')
resolve()
