q = int(input())
for _ in range(q):
    k,n,a,b = map(int, input().split())
    can_complete = k > b*n
    jp = (k -b*n -1)//(a -b)
    if not can_complete:
        print(-1)
    else:
        print(min(n,jp))
