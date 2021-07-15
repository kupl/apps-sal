n,r,avg = list(map(int, input().split(' ')))
L = []
for i in range(n) :
    x = list(map(int, input().split(' ')))
    L.append(x)

L.sort(key = lambda x : x[1])

s = 0
for i in L :
    s += i[0]

need = avg*n - s

if need <= 0 :
    ans = 0
else :   
    ans = 0
    start = 0
    while(need > 0) :
        a = L[start][0]
        b = L[start][1]
        k = r-a
        if k > need :
            ans += need*b
            need = 0
        else :
            ans += k*b
            need -= k
        start += 1
print(ans)

