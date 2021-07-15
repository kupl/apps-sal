K = int(input())
if K%2 == 0 or K%5 == 0:
    ans = -1
else:
    a = 1
    r = 7
    d = 70
    while True:
        if r%K ==0:
            ans = a
            break
        else:
            r, d, a = (r+d)%K, d*10%K, a+1
print(ans)
