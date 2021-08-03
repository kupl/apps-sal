n, m = list(map(int, input().split()))

x = list(map(int, input().split()))
y = list(map(int, input().split()))

ans = -1

if m == 1:
    for i in x:
        if abs(i - y[0]) > ans:
            ans = abs(i - y[0])
else:
    c = 0
    p = 0
    q = 1
    while c != n:
        #print("city %d" %(c))
        if (y[p] <= x[c]) and (y[q] >= x[c]):
            #print("city in between tower %d and %d" %(p, q))
            ans = max(ans, min((y[q] - x[c]), (x[c] - y[p])))
            c += 1
        elif y[q] < x[c]:
            #print("tower q %d lower than city" %q)
            if q != m - 1:
                #print("increase tower")
                p += 1
                q += 1
            else:
                #print("no more tower")
                ans = max(ans, x[c] - y[q])
                c += 1
        elif y[p] > x[c]:
            #print("tower p %d higher than city" %p)
            ans = max(ans, y[p] - x[c])
            c += 1

print(ans)
