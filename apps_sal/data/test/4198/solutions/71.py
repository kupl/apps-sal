a, b, x = map(int, input().split())
low = 0
high = 10**9
if a*10**9 + b*10 <= x:
    print(high)
else:
    while high - low > 1:
        n = (low + high)//2
        if a*n + b*len(str(n)) <= x:
            low = n
        else:
            high = n
    print(low)
