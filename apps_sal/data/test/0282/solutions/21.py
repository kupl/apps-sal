n, d = list(map(int, input().split()))
s = input()
a = 0
x = 0
while a <= n:
    k = min(d, n-a-1)
    place = s[a+1:a+k+1]
    if a == n-1:
        print(x)
        return
    elif '1' in place:
        a += k-place[::-1].index('1')
        x+=1
    else:
        print(-1)
        return

