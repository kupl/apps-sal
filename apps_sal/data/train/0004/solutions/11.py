from sys import stdin
input = stdin.readline


t = int(input())

for _ in range(t):

    n = int(input())
    a = list(map(int,input().split()))

    start = 0
    for i,v in enumerate(a):
        if v == 1:
            start = i
            break
    ans = [0]*-~n
    ans[n-1] = 1
    mx = 1
    l = start
    r = start

    def move(x):
        nonlocal l,r,mx
        if x:
            mx = max(a[r+1],mx)
            r += 1
        else:
            mx = max(a[l-1],mx)
            l -= 1


    while mx < n:
        if mx == r-l+1:
            ans[mx-1] = 1
        if l == 0:
            move(1)
        elif r == n-1:
            move(0)
        else:
            if a[l-1] > a[r+1]:
                move(1)
            else:
                move(0)

    print("".join(map(str,ans[:n])))




















