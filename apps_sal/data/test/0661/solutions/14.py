m, k = map(int, input().split())
if m == 0:
    if k == 0:
        print(0, 0)
    else:
        print(-1)
elif m == 1:
    if k == 0:
        print(0, 0, 1, 1)
    else:
        print(-1)
else:
    if k>=2**m:
        print(-1)
    else:
        L = [i for i in range(2 ** m) if i != k]
        ans = L + [k] + L[::-1] + [k]
        print(*ans, sep=' ')
    
