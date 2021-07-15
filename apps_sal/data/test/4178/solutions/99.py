n = int(input())
h = list(map(int,input().split()))
h = list(reversed(h))
can = True
if n == 1:
    print("Yes")
else:
    if h[0] < h[1]:
        if h[0] == h[1] - 1:
            h[1] -= 1
        else:
            can = False
    if can:
        for i in range(1,n-1):
            if h[i] == h[i+1] -1:
                h[i+1] -= 1
            if not h[i] >= h[i+1]:
                can = False
    print("Yes" if can else "No")
