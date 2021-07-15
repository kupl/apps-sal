a,b,f,k = map(int, input().split())

ans = 0
cb = b
for i in range(k):
    if i % 2 == 0:
        if f > cb:
            print(-1)
            return
        else:
            cb -= f
            if i != k-1:
                if cb < 2*(a-f):
                    ans += 1
                    cb = b
                cb -= a-f
            else:
                if cb < a-f:
                    ans += 1
                    cb = b
                cb -= a-f
                if cb < 0:
                    print(-1)
                    return
    else:
        if a-f > cb:
            print(-1)
            return
        else:
            cb -= a-f
            if i != k-1:
                if cb < 2*f:
                    ans += 1
                    cb = b
                cb -= f
            else:
                if cb < f:
                    ans += 1
                    cb = b
                cb -= f
                if cb < 0:
                    print(-1)
                    return
print(ans)    
