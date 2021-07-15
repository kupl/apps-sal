q=int(input())
for i in range(q):
    n, k = map(int, input().split())
    a=list(map(int, input().split()))
    mi = min(a)
    ma = max(a)
    if ma-mi>2*k:
        print(-1)
    else:
        print(mi+k)
